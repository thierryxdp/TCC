def maiores(lista, n):
    lista0 = list.insert(lista, 0, n)
    lista1 = list.sort(lista)
    return lista[n:]