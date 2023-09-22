def maiores(lista, n):
    lista.sort()
    if lista[:] <=n:
        del lista[:]
    return lista