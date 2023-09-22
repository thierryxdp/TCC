def maiores(lista, n):
    lista1 = lista + [n]
    lista1.sort()
    y = lista1.index(n)
    y1 = del(lista1[y:y])
    return y1