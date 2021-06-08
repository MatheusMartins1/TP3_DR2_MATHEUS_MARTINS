print("-" * 20, "Função 2", "-" * 20)
# 2.Escreva um programa em Python que leia um vetor de 5 números inteiros e mostre-os. (código)
numeros = []
for i in range(0,5):
    numeros.append(int(input("Informe um numero ")))

print(f'Os numeros inseridos foram {",".join(str(n) for n in numeros)}')
