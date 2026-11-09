from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from modelos_escola import Aluno, Turma
from datetime import date

engine = create_engine("sqlite:///escola.db", echo=True)

Session = sessionmaker(bind=engine)
sessao = Session()

turma = sessao.query(Turma).filter_by(
    nome_turma="3º Ano A"
).first()

print("\nTurma encontrada:")
print(turma)

alunos = sessao.query(Aluno).filter(
    or_(
        Aluno.data_nascimento > date(2005, 12, 31),
        Aluno.email.like("%@escola.com")
    )
).all()

print("\nAlunos encontrados:")

for aluno in alunos:
    print(aluno)

sessao.close()