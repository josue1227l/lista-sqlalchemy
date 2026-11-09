from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from modelos_loja import Produto

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

Session = sessionmaker(bind=engine)
sessao = Session()

produto = sessao.get(Produto, 1)

if produto:
    print("Produto encontrado:", produto)
else:
    print("Produto não encontrado!")

primeiro = sessao.query(Produto).first()

print("Primeiro produto:", primeiro)

resultado = sessao.execute(select(Produto)).scalars().all()

print("Lista de produtos:")

for produto in resultado:
    print(produto)

sessao.close()