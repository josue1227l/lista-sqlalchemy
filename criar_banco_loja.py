from sqlalchemy import create_engine
from modelos_loja import Base

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

Base.metadata.create_all(engine)

print("Banco da Loja Virtual criado com sucesso!")