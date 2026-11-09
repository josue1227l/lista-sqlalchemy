from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from modelos_loja import Produto

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

Session = sessionmaker(bind=engine)
sessao = Session()

resultado = sessao.query(
    Produto.categoria_id,
    func.avg(Produto.preco).label("preco_medio"),
    func.count(Produto.id).label("total_produtos")
).group_by(
    Produto.categoria_id
).having(
    func.avg(Produto.preco) > 250
).all()

print("\nRelatório de produtos por categoria:")

for categoria, media, total in resultado:
    print(f"Categoria: {categoria}")
    print(f"Preço médio: R$ {media:.2f}")
    print(f"Total de produtos: {total}")
    print("--------------------")

sessao.close()