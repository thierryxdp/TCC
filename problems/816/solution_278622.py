def maiores(lista, num):
    lista = lista + [num]
    lista.sort()
    posi = list.index(lista, num)
    return lista[num:]