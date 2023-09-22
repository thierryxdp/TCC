#funcao de achar repetiçoes
print("Este programa conta quantas vezes um item se repete em uma lista")
#lista que deve ser percorrida
lista=[1,4,3,3,2,3,3,3,3,5,4,6,6,7,6,8,8,7]
print(lista)
n=int(input("Escolha um item da lista: "))
if n in lista:
    repeticao=lista.count(n)
    print("Este item se repete", repeticao, "vezes.")
else:
    print("Esse item não aparece na lista")