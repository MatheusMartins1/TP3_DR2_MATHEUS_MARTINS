print("-" * 20, "Função 6", "-" * 20)
# 6.Escreva um programa em Python que leia diversas frases até a palavra “Sair” ser digitada. Indique quais frases apresentam a palavra “eu”. (código)
frases = []
while True:
    frase = str(input("Escreva Uma frase: "))
    if frase.lower() == "sair":
        break
    else:
        if "eu" in frase.replace(" ","").lower():
            frases.append(frase)
print("As seguintes frases contem a palavra 'eu' \n:{0}".format('\n'.join(frases)))