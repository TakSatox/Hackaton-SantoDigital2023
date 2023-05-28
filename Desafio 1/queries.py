from database import SessionLocal
from calendar import month_name
from sqlalchemy.sql import func
import pandas
from models import Product, ProductCategory, ProductSubcategory, Sales, Customer, Territory, Return


session = SessionLocal()

#Q1 -  Quais são os 10 produtos mais vendidos (em quantidade) na categoria "Bicicletas"?
result = session.query(Sales.productkey, Product.productname, func.sum(Sales.orderquantity)) \
    .join(Product).join(ProductSubcategory).join(ProductCategory).filter(ProductCategory.categoryname=='Bikes') \
    .group_by(Sales.productkey, Product.productname).order_by(func.sum(Sales.orderquantity).desc()).limit(10).all()

result = [result[1] for result in result]

df = pandas.DataFrame(result, columns=['BIKESMAISVENDIDASTOP10'])
df.to_csv('.\csvexports\Bikesmaisvendidas.csv', index=False)


#Q2 - Qual é o cliente que tem o maior número de pedidos realizados?
result = session.query(Sales.customerkey, Customer.prefix, Customer.firstname, Customer.lastName, \
            func.count(Sales.orderkey)).join(Customer).filter(Sales.customerkey == Customer.customerkey) \
            .group_by(Sales.customerkey, Customer.firstname).order_by(func.count(Sales.orderkey).desc()).first()

result = [result[1]+' '+result[2]+' '+result[3]]

df = pandas.DataFrame(result, columns=['CLIENTETOP1PEDIDOS'])
df.to_csv('.\csvexports\Clientemaiorquantpedidos.csv', index=False)


#Q3 - Em qual mês do ano ocorrem mais vendas (em valor total)?
result = session.query(func.extract('month', Sales.orderdate), func.sum(Sales.orderquantity * Product.productprice)) \
            .join(Product).group_by(func.extract('month', Sales.orderdate))\
            .order_by(func.sum(Sales.orderquantity * Product.productprice).desc()).first()

result = [month_name[result[0]]]

df = pandas.DataFrame(result, columns=['MESTOP1VENDAS'])
df.to_csv('.\csvexports\Mesmaiorvalortoalvendas.csv', index=False)


#Q4 - Quais regiões que tiveram vendas com valores acima da média no último ano fiscal.
'''Conforme orientado por Liane, ajustei a pergunta para que fosse possível responder o mais próximo possível visto que não
   há a tabela de vendedores.'''
result = session.query(Territory.country, Territory.region, func.sum(Sales.orderquantity)) \
    .join(Sales).filter(Sales.orderdate >= '2017-01-01', Sales.orderdate < '2018-01-01') \
    .group_by(Territory.country, Territory.region).having(func.sum(Sales.orderquantity) > (func.sum(Sales.orderquantity) / 12)).all()

result = [(result[0]+': '+result[1]) for result in result]

df = pandas.DataFrame(result, columns=['REGIOESACIMAMEDIA'])
df.to_csv('.\csvexports\Regioesacimadamedia.csv', index=False)


#Q5 - Quais os 20 clientes com menor quantidade de pedidos? (Para fins de marketing direcionado)
result = session.query(Sales.customerkey, Customer.prefix, Customer.firstname, Customer.lastName, \
            func.count(Sales.orderkey)).join(Customer).filter(Sales.customerkey == Customer.customerkey) \
            .group_by(Sales.customerkey, Customer.firstname).order_by(func.count(Sales.orderkey).asc()).limit(20).all()

result = [(result[1]+' '+result[2]+' '+result[3]) for result in result]

df = pandas.DataFrame(result, columns=['CLIENTESTOP20MENORCOMPRA'])
df.to_csv('.\csvexports\Clientesmenorquantcompra.csv', index=False)

