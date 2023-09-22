def maiores(lista, n):
    lista.sort()
    if lista[0] <=n:
        del lista[0]
    return lista