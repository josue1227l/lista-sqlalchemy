from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos_loja import Produto

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

Session = sessionmaker(bind=engine)
sessao = Session()

consulta = sessao.query(Produto).filter_by(em_estoque=True)

consulta = consulta.add_columns(
    (Produto.preco * 0.85).label("preco_promocional")
)

resultado = consulta.all()

print("\nProdutos em promoção:")

for produto, preco_promocional in resultado:
    print(f"Produto: {produto.nome}")
    print(f"Preço original: R$ {produto.preco:.2f}")
    print(f"Preço promocional: R$ {preco_promocional:.2f}")
    print("----------------------")

sessao.close()