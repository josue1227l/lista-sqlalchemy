from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos_loja import Categoria, Produto

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

Session = sessionmaker(bind=engine)
sessao = Session()

categorias = ["Informática", "Eletrônicos", "Acessórios"]

for nome in categorias:
    categoria = sessao.query(Categoria).filter_by(nome=nome).first()

    if not categoria:
        sessao.add(Categoria(nome=nome))

sessao.commit()

informatica = sessao.query(Categoria).filter_by(nome="Informática").first()
eletronicos = sessao.query(Categoria).filter_by(nome="Eletrônicos").first()
acessorios = sessao.query(Categoria).filter_by(nome="Acessórios").first()

produtos = [
    Produto(
        nome="Notebook Gamer",
        codigo_barras="100001",
        preco=3500.00,
        em_estoque=True,
        categoria_id=informatica.id
    ),
    Produto(
        nome="Mouse Gamer",
        codigo_barras="100002",
        preco=150.00,
        em_estoque=True,
        categoria_id=acessorios.id
    ),
    Produto(
        nome="Teclado Mecânico",
        codigo_barras="100003",
        preco=280.00,
        em_estoque=True,
        categoria_id=acessorios.id
    ),
    Produto(
        nome="Monitor",
        codigo_barras="100004",
        preco=900.00,
        em_estoque=False,
        categoria_id=eletronicos.id
    ),
    Produto(
        nome="Fone Bluetooth",
        codigo_barras="100005",
        preco=200.00,
        em_estoque=True,
        categoria_id=eletronicos.id
    )
]

for produto in produtos:
    existente = sessao.query(Produto).filter_by(
        codigo_barras=produto.codigo_barras
    ).first()

    if not existente:
        sessao.add(produto)

sessao.commit()

print("\nDados de teste cadastrados com sucesso!")

sessao.close()