from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


config = {
    'User': 'root',
    'Password': '1234',
    'Host': 'localhost',
    'Port': '32787',
}


#Cria um link de conexão para o banco de dados mysql onde root é o usuário, 1234 a senha, localhost o endereço de ip raiz, 3306
#a porta e advetureworks o banco de dados em si.
#A porta deve ser especificada caso for rodar no docker.
engine = create_engine(f'mysql+pymysql://{config["User"]}:{config["Password"]}@{config["Host"]}:{config["Port"]}/adventureworks')

#Utilizando o sessionmaker vinculado ao engine, crio um "construtor" de sessões através do SessionLocal().
#Dessa forma consigo criar várias sessões diferentes caso desejar. As sessões são utilizadas para de fato
#realizar alguma comunicação com o banco de dados.
SessionLocal = sessionmaker(bind=engine)

#Declarando o declarative_base() para que possa usá-lo nas classes model como super classe que serve para fazer uma espécie de
#interface entre os objetos do python com as tabelas do banco de dados.
Base = declarative_base()