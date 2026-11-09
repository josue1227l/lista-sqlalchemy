from sqlalchemy import create_engine
from modelos_escola import Base

engine = create_engine("sqlite:///escola.db", echo=True)

Base.metadata.create_all(engine)

for tabela in Base.metadata.sorted_tables:
    print(f"\nTabela: {tabela.name}")
    print(str(tabela.compile(engine)))

print("\nBanco da Escola criado com sucesso!")