from sqlalchemy import create_engine, exists
from sqlalchemy.orm import sessionmaker
from modelos_escola import Aluno, Turma

engine = create_engine("sqlite:///escola.db", echo=True)

Session = sessionmaker(bind=engine)
sessao = Session()

turma_id = 5

resultado = sessao.query(Turma).filter(
    Turma.id == turma_id
).filter(
    exists().where(Aluno.turma_id == Turma.id)
).first()

if resultado:
    print("Existem alunos matriculados nessa turma!")
else:
    print("Não existem alunos matriculados nessa turma.")

sessao.close()