from sqlalchemy import create_engine, exists
from sqlalchemy.orm import sessionmaker
from modelos_loja import Produto, Categoria

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

Session = sessionmaker(bind=engine)
sessao = Session()

categoria_id = 1

resultado = sessao.query(Categoria).filter(
    Categoria.id == categoria_id
).filter(
    exists().where(Produto.categoria_id == Categoria.id)
).first()

if resultado:
    print("A categoria possui produtos associados!")
else:
    print("A categoria não possui produtos associados.")

sessao.close()