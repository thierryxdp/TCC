def maiores(lista, n):
    list.sort(lista)
    while len(lista) > 0 and lista[0] < n:
        del lista[0]
    return lista