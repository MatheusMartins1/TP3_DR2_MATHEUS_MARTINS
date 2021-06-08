import random
import numpy as np
from string import ascii_lowercase
print("-" * 20, "Função 7", "-" * 20)
# 7.Escreva um programa em Python que realiza operações de inclusão e remoção em listas. Seu programa deve perguntar ao usuário qual operação deseja fazer: (código)
# a.Mostrar lista;
# b.Incluir elemento;
# c.Remover elemento;
# d.Apagar todos os elementos da lista.
# Se a opção for a alternativa (a), seu programa deve apenas mostrar o conteúdo da lista. Se a opção for a alternativa (b), seu programa deve pedir o valor do elemento a ser incluído. Se a opção for a alternativa (c), seu programa deve pedir o valor do elemento a ser removido. E se a opção for a alternativa (d), deve-se apenas exibir se a operação foi concluída.

lista = list(np.random.randint(1, 300, size=np.random.randint(6, 30)))

loop = True
while loop:
    print("\nOperações:",
        "\na.Mostrar lista;", 
        "\nb.Incluir elemento;",
        "\nc.Remover elemento;", 
        "\nd.Apagar todos os elementos da lista.",
        "\ne.Sair do loop.\n")

    operacao = str(input("informe a operacao desejada: ")).lower()

    if operacao == "a":
        print('\nlista:',lista)
    elif operacao == "b":
        elemento = input("\ninforme o elemento a ser incluido: ")
        lista.append(elemento)
    elif operacao == "c":
        
        elemento = input("\ninforme o elemento a ser excluido: ")
        elemento = str(elemento) if elemento.lower() in ascii_lowercase else int(elemento)
        try:
            lista.pop(lista.index(elemento))
            print(f"Elemento {elemento} removido com sucesso")
        except Exception as e:
            print("\nO elemento nao existe na lista")
    elif operacao == "d":
        lista.clear()
        print("\nTodos os elementos foram removidos da lista")    
    elif operacao == "e":
        loop = False
        print("\nFim do loop")
    else:
        print("\nOperação inválida")
