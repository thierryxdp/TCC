def maiores(lista, n):
    lista.sort()
    lista[:n]=lista
    return lista