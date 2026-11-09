from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos_loja import Produto

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

Session = sessionmaker(bind=engine)
sessao = Session()

total = sessao.query(Produto).count()

print("Total de produtos:", total)

categorias = sessao.query(Produto.categoria_id).distinct().all()

print("\nCategorias diferentes:")

for categoria in categorias:
    print(categoria)

produtos = sessao.query(Produto).order_by(
    Produto.preco.desc()
).limit(5).offset(5).all()

print("\nSegunda página - Produtos mais caros:")

for produto in produtos:
    print(produto)

sessao.close()