def maiores(lista, n):
    lista.sort()
    lista[:n-1]=lista
    return lista