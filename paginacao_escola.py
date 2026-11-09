from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos_escola import Aluno

engine = create_engine("sqlite:///escola.db", echo=True)

Session = sessionmaker(bind=engine)
sessao = Session()

total = sessao.query(Aluno).count()

print("Total de alunos:", total)

alunos = sessao.query(Aluno).order_by(
    Aluno.nome.asc()
).all()

print("\nAlunos em ordem alfabética:")

for aluno in alunos:
    print(aluno)

pagina_atual = 3
tamanho_pagina = 10

offset = (pagina_atual - 1) * tamanho_pagina

alunos_paginados = sessao.query(Aluno).order_by(
    Aluno.nome.asc()
).offset(offset).limit(tamanho_pagina).all()

print("\nTerceira página:")

for aluno in alunos_paginados:
    print(aluno)

sessao.close()