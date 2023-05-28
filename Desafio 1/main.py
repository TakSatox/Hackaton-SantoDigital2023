from database import engine
from models import Base

#   Irá criar todas as tabelas do models
Base.metadata.create_all(bind=engine)
