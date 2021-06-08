print("-" * 20, "Função 4", "-" * 20)
# 4.Escreva um programa em Python que leia um vetor de números de tamanho t. Leia t previamente. Em seguida, faça seu programa verificar quantos números iguais a 0 existem nele. (código)
t = int(input("Informe o tamanho do vetor "))
vetor = []
for num in range(0,t):
    vetor.append(int(input("Informe um numero ")))
qntd_zeros = sum([1 for i in vetor if i == 0])
print(f'Os vetor possui {t} posições, e nele há contido {qntd_zeros} numeros 0')
