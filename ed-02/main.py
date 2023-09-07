from dataclasses import dataclass
import random


@dataclass
class Aluno:
    nome: str
    matricula: int
    notas: list[float]

    def get_media(self) -> float:
        return sum(self.notas) / len(self.notas)


# Lista de nomes de alunos
nomes_alunos = ["João", "Maria", "Pedro", "Ana", "Carlos", "Isabel", "Luís", "Rita", "Miguel", "Sofia"]

alunos = []

for i in range(10):
    nome = random.choice(nomes_alunos)  # Escolhe um nome aleatório da lista
    nomes_alunos.remove(nome)  # Remove o nome escolhido da lista
    matricula = i + 1
    notas = [random.randint(0, 10) for _ in range(3)]
    aluno = Aluno(nome, matricula, notas)
    alunos.append(aluno)

alunos_ordenados_nome = sorted(alunos, key=lambda x: x.nome)
print("Alunos em ordem alfabética:")
for aluno in alunos_ordenados_nome:
    print(f"{aluno.nome} - Média: {aluno.get_media():.2f}")

alunos_ordenados_media = sorted(alunos, key=lambda x: x.get_media(), reverse=True)
print("\nAlunos em ordem decrescente de média:")
for aluno in alunos_ordenados_media:
    print(f"{aluno.nome} - Média: {aluno.get_media():.2f}")

top_alunos = alunos_ordenados_media[:2]
piores_alunos = alunos_ordenados_media[-2:]

print("\nDois alunos com maior média:")
for aluno in top_alunos:
    print(f"{aluno.nome} - Média: {aluno.get_media():.2f}")

print("\nDois alunos com menor média:")
for aluno in piores_alunos:
    print(f"{aluno.nome} - Média: {aluno.get_media():.2f}")

media_turma = sum(aluno.get_media() for aluno in alunos) / len(alunos)
print(f"\nMédia da turma: {media_turma:.2f}")

print("\nAlunos abaixo da média da turma:")
for aluno in alunos:
    if aluno.get_media() < media_turma:
        print(f"{aluno.nome} - Média: {aluno.get_media():.2f}")
