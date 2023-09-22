def maiores(lista):
    lista1 = lista[0]
    list.sort(lista1)
    list.reverse(lista1)
    lista2 = []
    while list.pop(lista1, 0) > lista[1]:
        lista2.append(list.pop(lista1, 0))
    return lista2