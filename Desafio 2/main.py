from fastapi import FastAPI, HTTPException
from calendar import month_name
from sqlalchemy.sql import func
from pydantic import BaseModel
from starlette import status
from database import engine, SessionLocal
from models import Base, Product, Sales, ProductCategory, ProductSubcategory, Customer, Territory


app = FastAPI()
Base.metadata.create_all(bind=engine)
session = SessionLocal()


''' Essa classe serve para validar os dados enviados através do JSON no body da requisição. Isso significa que mesmo que sejam inseridos
    outras chaves:valor, não seriam coletadas. Apenas são coletados o que é definido nesta classe'''
class ProductsRequest(BaseModel):
    productname: str 
    productdescription: str
    productsize: str
    productcost: float
    modelname: str
    productsubcategorykey: int
    productsku: str
    productcolor: str
    productstyle: str
    productprice: float



### Tarefa 1


@app.post('/products', status_code=status.HTTP_204_NO_CONTENT)
    #Recebe o JSON do body como a variável product e para validar os dados utilizamos neste caso o ProductsRequest
def create(product: ProductsRequest):
    try:
        #Transforma o JSON em dicionário, em seguida desempacota com o kwargs seguindo as variáveis da classe Product.
        new_product = Product(**product.dict())
        #Atravéss do session adiciona o produto.
        session.add(new_product)
        #Para salvar de fato no banco de dados é feito o commit.
        session.commit()
        #Além do status code de sucesso NO CONTENT, também retornando uma mensagem.
        return {'message': 'Product created succesfully'}
    except:
        '''Para caso acontecer algum erro é feito um session.rollback para que a session volte para o último estado e não
           ocorra erro ao utilizá-lo novamente. Assim evita-se ter que reiniciar o servidor do uvicorn. Esse erro é mais 
           importante de ser tratado no método delete.'''
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get('/products', status_code=status.HTTP_200_OK)
def get_all_products():
    try:
        #Recebe uma lista de todos produtos da tabela Product
        found_product = session.query(Product).all() 
        #Se a lista não for vazia será retornada e caso for, será levantado com raise statuscode 404 not found
        if found_product != []: 
            return found_product
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    except:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get('/products/{id}', status_code=status.HTTP_200_OK)
def get_one_product(id: int):
    try:
        #Com o first() é retornado apenas um registro que é justamente o produto com o id correspondente.
        found_product = session.query(Product).filter(Product.productkey == id).first()    
        if found_product != None:
            return found_product
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    except:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


##No método put, é recebido tanto o id no path quanto o JSON no body
@app.put('/products/{id}', status_code=status.HTTP_204_NO_CONTENT)
def update_product(id: int, product: ProductsRequest):
    #Primeiramente procura o produto correspondente.
    found_product = session.query(Product).filter(Product.productkey == id).first()
    try:
        if found_product != None:

            #Faz o mesmo procedimento que no post.
            new_product = Product(**product.dict())
            
            #Recebe coluna por coluna cada valor.
            found_product.productsubcategorykey  = new_product.productsubcategorykey        
            found_product.productsku = new_product.productsku
            found_product.productname = new_product.productname
            found_product.modelname = new_product.modelname
            found_product.productdescription = new_product.productdescription
            found_product.productcolor = new_product.productcolor
            found_product.productsize = new_product.productsize
            found_product.productstyle = new_product.productstyle
            found_product.productcost = new_product.productcost
            found_product.productprice = new_product.productprice

            #Adiciona novamente o produto que foi alterado
            session.add(found_product)
            #Commita para salvar no banco de dados
            session.commit()
            return {'message': 'Product updated succesfully'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    except:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)



@app.delete('/products/{id}', status_code=status.HTTP_200_OK)
def delete_product(id: int):
    found_product = session.query(Product).filter(Product.productkey == id).first()
    try:
        if found_product != None:
            session.delete(found_product)
            session.commit()
            return {'message': 'Product deleted succesfully'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    except:
        '''Esse session.rollback é importante aqui pois caso na requisição seja solicitado a exclusão de um produto que está
           relacionado com algum registro da tabela returns, não é possível excluir a não ser que todos os registros da tabela
           returns que estejam relacionados ao produto sejam excluídos antes.'''
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)



###### Rotas da tarefa 3

#Exatamente as mesmas queries realizadas no desafio, porém adaptadas aos endpoints.

@app.get('/sales/top-products/{category}')
def get_products(category: str):
    result = session.query(Sales.productkey, Product.productname, func.sum(Sales.orderquantity)) \
    .join(Product).join(ProductSubcategory).join(ProductCategory).filter(ProductCategory.categoryname==category) \
    .group_by(Sales.productkey, Product.productname).order_by(func.sum(Sales.orderquantity).desc()).limit(10).all()
    
    result = [result[1] for result in result]
    return result


@app.get('/sales/best-customer')
def get_customer():
    result = session.query(Sales.customerkey, Customer.prefix, Customer.firstname, Customer.lastName, \
            func.count(Sales.orderkey)).join(Customer).filter(Sales.customerkey == Customer.customerkey) \
            .group_by(Sales.customerkey, Customer.firstname).order_by(func.count(Sales.orderkey).desc()).first()

    result = [result[1]+' '+result[2]+' '+result[3]]
    return result


@app.get('/sales/busiest_month')
def get_month():
    result = session.query(func.extract('month', Sales.orderdate), func.sum(Sales.orderquantity * Product.productprice)) \
            .join(Product).group_by(func.extract('month', Sales.orderdate))\
            .order_by(func.sum(Sales.orderquantity * Product.productprice).desc()).first()

    result = [month_name[result[0]]]
    return result


@app.get('/sales/top-region-sellers')
def get_territory():
    result = session.query(Territory.country, Territory.region, func.sum(Sales.orderquantity)) \
    .join(Sales).filter(Sales.orderdate >= '2017-01-01', Sales.orderdate < '2018-01-01') \
    .group_by(Territory.country, Territory.region).having(func.sum(Sales.orderquantity) > (func.sum(Sales.orderquantity) / 12)).all()

    result = [(result[0]+': '+result[1]) for result in result]
    return result
