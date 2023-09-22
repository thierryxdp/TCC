def maiores(lista, n):
    lista1 = lista + [n]
    lista1.sort()
    y = lista1.index(n)
    del(lista1[0:y])
    return lista1