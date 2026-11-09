from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from modelos_escola import Aluno

engine = create_engine("sqlite:///escola.db", echo=True)

Session = sessionmaker(bind=engine)
sessao = Session()

aluno = sessao.get(Aluno, 1)

if aluno:
    print("Matrícula:", aluno.matricula)
    print("Nome:", aluno.nome)
else:
    print("Aluno não encontrado!")

alunos = sessao.query(Aluno).all()

print("\nTodos os alunos:")

for aluno in alunos:
    print(aluno)

resultado = sessao.execute(select(Aluno)).all()

print("\nResultado sem scalars():")
print(resultado)

resultado = sessao.execute(select(Aluno)).scalars().all()

print("\nResultado com scalars():")
print(resultado)

sessao.close()