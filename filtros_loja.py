from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos_loja import Produto

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

Session = sessionmaker(bind=engine)
sessao = Session()

produtos = sessao.query(Produto).filter_by(em_estoque=True).all()

print("\nProdutos disponíveis em estoque:")

for produto in produtos:
    print(produto)

produtos_gamer = sessao.query(Produto).filter(
    Produto.preco > 100,
    Produto.nome.ilike("%Gamer%")
).all()

print("\nProdutos Gamer com preço acima de R$ 100:")

for produto in produtos_gamer:
    print(produto)

sessao.close()