print("-" * 20, "Função 8", "-" * 20)
# Faça uma função um programa em Python que simula um lançamento de dados.
# Lance o dado 100 vezes e armazene os resultados em um vetor. 
# Depois, mostre quantas vezes cada valor foi conseguido. 
# Dica: use um vetor de contadores (1-6) e uma função do módulo 'random' de Python para gerar números aleatórios, simulando os lançamentos dos dados. (código)
import random
import numpy as np
from collections import Counter

resultados = []
for i in (range(1,100)):
    resultado = np.random.randint(1, 7)
    resultados.append(resultado)

contagem = dict(sorted(Counter(resultados).items(), key=lambda item: item[1],reverse=True))

print('Resultados:',resultados,"\n\n",'Contagem:',contagem)