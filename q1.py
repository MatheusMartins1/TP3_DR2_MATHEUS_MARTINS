print("-" * 20, "Função 1", "-" * 20)

# a.Crie uma lista vazia;
list1 = []
# b.Adicione os elementos: 1, 2, 3, 4 e 5,  usando append();
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
# c.Imprima a lista;
print(list1)
# d.Agora, remova os elementos 3 e 6 (não esqueça de checar se eles estão na lista);
for i in list1:
    # print(i)
    if i in(3,6):
        print(i)
        list1.remove(list1.index(i+1))
# e.Imprima a lista modificada;
print("e.Imprima a lista modificada:", list1)
# f.Imprima também o tamanho da lista usando a função len();
print("Tamanho da lista:", len(list1))
# g.Altere o valor do último elemento para 6 e imprima a lista modificada.
list1[len(list1)-1] = 6
print(list1)