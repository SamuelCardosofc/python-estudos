alunos = {}
aluno = {
    "nome": "Ana",
    "ra": "123",
    "notas": [7.5, 8.0, 9.0]
}

print(aluno["nome"])
print(aluno["notas"])

aluno["nome"] = "Ana Paula"

aluno["curso"] = "DS"

for chave, valor in aluno.items():
    print(chave, ":", valor)

alunos = []

aluno = {}
aluno["ra"] = "123"
aluno["nome"] = "Ana"
aluno["notas"] = [7.5, 8.0]

alunos.append(aluno)  # aqui sim é append


