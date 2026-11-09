from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

with engine.connect() as conexao:

    resultado = conexao.execute(
        text("SELECT 'Sistema de Loja Virtual Conectado com Sucesso!'")
    )

    print(resultado.scalar())