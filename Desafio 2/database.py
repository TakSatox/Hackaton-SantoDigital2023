from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


'''Mesma configuração do desafio1, tendo como diferença apenas o host. Para que seja possível acessar o container do docker através 
do localhost, é necessário passar o host.docker.internal no host porque o container em si é um ambiente isolado da máquina'''
config = {
    'User': 'root',
    'Password': '1234',
    'Host': 'host.docker.internal',
    'Port': '32787',
}


engine = create_engine(f'mysql+pymysql://{config["User"]}:{config["Password"]}@{config["Host"]}:{config["Port"]}/adventureworks')

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()