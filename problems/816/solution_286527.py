def maiores(lista, numero):
    list.append(lista, numero)
    list.sort(lista)
    index = lista.index(numero)
    nova_lista = lista[index+1:]
    
    return nova_lista

lista1 = [1,56,23,4,12]
lista2 = [10, 50,134, 14]
lista3 = [90, 2, 15,73, 8, 7]

maiores(lista1, 10)
maiores(lista2, 40)
maiores(lista3, 14)