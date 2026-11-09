from sqlalchemy import create_engine, func, cast, Integer
from sqlalchemy.orm import sessionmaker
from datetime import date
from modelos_escola import Aluno

engine = create_engine("sqlite:///escola.db", echo=True)

Session = sessionmaker(bind=engine)
sessao = Session()

turma_id = 1

ano_atual = date.today().year

consulta = sessao.query(Aluno).filter(Aluno.turma_id == turma_id)

consulta = consulta.add_columns(
    (
        ano_atual - cast(func.strftime("%Y", Aluno.data_nascimento), Integer)
    ).label("idade_aproximada")
)

resultado = consulta.all()

print("\nAlunos e suas idades aproximadas:")

for aluno, idade in resultado:
    print(f"Nome: {aluno.nome}")

    if idade is not None:
        print(f"Idade aproximada: {idade} anos")
    else:
        print("Idade aproximada: não informada")

    print("----------------------")

sessao.close()