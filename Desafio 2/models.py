from database import Base
from sqlalchemy import Column, Integer, String, Date, Float, Enum, ForeignKey

##  Utilizei as mesmas classes do desafio1, então é a mesma explicação.

class Calendar(Base):
    __tablename__ = 'calendar'

    calendarkey = Column(Integer, primary_key=True)
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
