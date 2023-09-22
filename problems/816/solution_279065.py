def maiores(lista, n):
    list.sort(lista)
    while lista[0] < n:
        del lista[0]
    return lista