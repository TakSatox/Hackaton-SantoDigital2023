from database import Base
from sqlalchemy import Column, Integer, String, Date, Float, Enum, ForeignKey


#   Em models, crio as classes que irão representar cada tabela no banco de dados. Para tal, preciso definir que essas classes
#   extendem o Base declarado em database.py.
class Calendar(Base):
    #   Informo o nome da tabela no banco de dados
    __tablename__ = 'calendar'

    #   Precisei acrescenter uma chave primária porque o SQLAlchemy não aceita criar tabelas sem definir uma como chave primária.
    calendarkey = Column(Integer, primary_key=True)
    ''' Para definir que essas variáveis são colunas, atribuo a elas a função Column() e nos argumentos informo o tipo de dado
        da coluna e também posso aplicar algumas restrições que há no próprio mysql. Basta importar tudo do sqlalchemy.'''
    date = Column(Date)


class Customer(Base):
    __tablename__ = 'customers'

    customerkey = Column(Integer, primary_key=True)
    prefix = Column(String(100))
    firstname = Column(String(30))
    lastName = Column(String(30))
    birthdate = Column(Date)
    maritalstatus = Column(String(1))
    gender = Column(String(1), Enum('M', 'F'))
    emailaddress = Column(String(50))
    annualincome = Column(String(20))
    totalchildren = Column(Integer)
    educationlevel = Column(String(50))
    occupation = Column(String(50))
    homeowner = Column(String(1))


class ProductCategory(Base):
    __tablename__ = 'productcategories'

    productcategorykey = Column(Integer, primary_key=True)
    categoryname = Column(String(50))


class ProductSubcategory(Base):
    __tablename__ = 'productsubcategories'

    productsubcategorykey = Column(Integer, primary_key=True)
    subcategoryname = Column(String(50))
    '''Como mencionado na primeira classe, posso aplicar restrições também. Nesse caso apliquei a restrição de chave estrangeira
       criando um relacionamento entre ProductSubcategory e ProductCategory.'''
    productcategorykey = Column(Integer, ForeignKey('productcategories.productcategorykey'))
    

class Product(Base):
    __tablename__ = 'products'

    productkey = Column(Integer, primary_key=True)
    productsubcategorykey = Column(Integer, ForeignKey('productsubcategories.productsubcategorykey'))
    productsku = Column(String(50))
    productname = Column(String(50))
    modelname = Column(String(50))
    productdescription = Column(String(500))
    productcolor = Column(String(50))
    productsize = Column(String(50))
    productstyle = Column(String(50))
    productcost = Column(Float)
    productprice = Column(Float)


class Territory(Base):
    __tablename__ = 'territories'

    salesterritorykey = Column(Integer, primary_key=True)
    region = Column(String(50))
    country = Column(String(50))
    continent = Column(String(50))


class Return(Base):
    __tablename__ = 'returns'

    returnkey = Column(Integer, primary_key=True)
    returndate = Column(Date)
    territorykey = Column(Integer, ForeignKey('territories.salesterritorykey'))
    productkey = Column(Integer, ForeignKey('products.productkey'))
    returnquantity = Column(Integer)


class Sales(Base):
    __tablename__ = 'sales'

    orderkey = Column(Integer, primary_key=True, autoincrement=True)
    orderdate = Column(Date)
    stockdate = Column(Date)
    ordernumber = Column(String(100))
    productkey = Column(Integer, ForeignKey('products.productkey'))
    customerkey = Column(Integer, ForeignKey('customers.customerkey'))
    territorykey = Column(Integer, ForeignKey('territories.salesterritorykey'))
    orderlineitem = Column(Integer)
    orderquantity = Column(Integer)
