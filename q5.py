print("-" * 20, "Função 5", "-" * 20)
# 5.Escreva um programa em Python que leia nomes de alunos e suas alturas em metros até que um nome de aluno seja o código de saída “Sair”. O programa deve possuir uma função que indica todos os alunos que tenham altura acima da média (a média aritmética das alturas de todos os alunos lidos). (código)
alunos = {}
i=1
while True:
    nome = str(input(f"Escreva o nome do {i}° aluno "))
    if nome.lower() == "sair":
        break
    else:
        alunos[i] = {}
        alunos[i]["nome"] = nome
        alunos[i]["altura"] = float(input(f"Escreva a altura do {i}° aluno "))
        i += 1

alturas = [alunos[m]["altura"] for m in alunos]
media = sum(alturas)/len(alturas)

giga_alunos = [alunos[a]["nome"] for a in alunos if alunos[a]["altura"] > media]

print(f"A média de altura é {media} | Os alunos acima da média são {','.join(giga_alunos)}")