from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from modelos_escola import Aluno

engine = create_engine("sqlite:///escola.db", echo=True)

Session = sessionmaker(bind=engine)
sessao = Session()

resultado = sessao.query(
    Aluno.turma_id,
    func.count(Aluno.id).label("total_alunos")
).group_by(
    Aluno.turma_id
).having(
    func.count(Aluno.id) > 30
).all()

print("\nRelatório de alunos por turma:")

for turma, total in resultado:
    print(f"Turma: {turma}")
    print(f"Total de alunos: {total}")
    print("--------------------")

sessao.close()