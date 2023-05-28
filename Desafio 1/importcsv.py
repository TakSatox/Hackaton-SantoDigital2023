from models import Calendar, Customer, Product, ProductCategory, ProductSubcategory, Territory, Return, Sales
from database import engine
import pandas

#  Utilizando a biblioteca pandas para facilitar no import dos arquivos csv nas tabelas
#  Na função read_csv passamos como argumentos o caminho onde está o arquivo csv e outros para inserir regras na leitura dos dados

'''Pode-se observar que nas tabelas que possuem data utilizei o parse_dates que transforma as datas contidas no csv em um formato
   aceito pelo mysql. Por exemplo a data no csv está em MM-DD-YYYY, porém o mysql só aceita o formato YYYY-MM-DD.'''

'''No to_sql devemos colocar no argumento a conexão (con) que no caso é com o engine e o nome da tabela que estou coletando diretamente
   da classe através por exemplo do Calendar.__tablename__.'''

'''O if_exists informa o que fazer caso a tabela já existir no banco de dados. No caso do 'append', define que deve apenas ser inserido
   os dados na tabela.'''

'''O index define se será inserido o index de cada linha. Como nas classes do models.py não criei uma coluna nomeada index, no caso se 
   fosse index=True seria retornado o erro de não existir tal coluna.'''

df = pandas.read_csv('.\csvimports\AdventureWorks_Calendar.csv', parse_dates=['Date'])

df.to_sql(con=engine, name=Calendar.__tablename__, if_exists='append', index=False)

#  Nesse read_csv adicionei o argumento encoding='latin-1' porque há caracteres não compatíveis. Com o encoding='latin-1', faz com que seja.
df = pandas.read_csv('.\csvimports\AdventureWorks_Customers.csv', parse_dates=['BirthDate'], encoding='latin-1')
df.to_sql(con=engine, name=Customer.__tablename__, if_exists='append', index=False)


df = pandas.read_csv('.\csvimports\AdventureWorks_Product_Categories.csv')
df.to_sql(con=engine, name=ProductCategory.__tablename__, if_exists='append', index=False)


df = pandas.read_csv('.\csvimports\AdventureWorks_Product_Subcategories.csv')
df.to_sql(con=engine, name=ProductSubcategory.__tablename__, if_exists='append', index=False)

df = pandas.read_csv('.\csvimports\AdventureWorks_Products.csv')
df.to_sql(con=engine, name=Product.__tablename__, if_exists='append', index=False)


df = pandas.read_csv('.\csvimports\AdventureWorks_Territories.csv')
df.to_sql(con=engine, name=Territory.__tablename__, if_exists='append', index=False)


df = pandas.read_csv('.\csvimports\AdventureWorks_Returns.csv', parse_dates=['ReturnDate'])
df.to_sql(con=engine, name=Return.__tablename__, if_exists='append', index=False)


df = pandas.read_csv('.\csvimports\AdventureWorks_Sales_2015.csv', parse_dates=['OrderDate', 'StockDate'])
df.to_sql(con=engine, name=Sales.__tablename__, if_exists='append', index=False)
df = pandas.read_csv('.\csvimports\AdventureWorks_Sales_2016.csv', parse_dates=['OrderDate', 'StockDate'])
df.to_sql(con=engine, name=Sales.__tablename__, if_exists='append', index=False)
df = pandas.read_csv('.\csvimports\AdventureWorks_Sales_2017.csv', parse_dates=['OrderDate', 'StockDate'])
df.to_sql(con=engine, name=Sales.__tablename__, if_exists='append', index=False)

