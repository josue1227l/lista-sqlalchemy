from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos_loja import Produto, Categoria

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

Session = sessionmaker(bind=engine)
sessao = Session()

resultado = sessao.query(
    Produto.nome,
    Categoria.nome
).join(
    Categoria, Produto.categoria_id == Categoria.id
).all()

print("\nProdutos e suas categorias:")

for produto, categoria in resultado:
    print(f"Produto: {produto} | Categoria: {categoria}")

categorias = sessao.query(Categoria).outerjoin(
    Produto, Categoria.id == Produto.categoria_id
).filter(
    Produto.id == None
).all()

print("\nCategorias sem produtos:")

for categoria in categorias:
    print(categoria.nome)

sessao.close()