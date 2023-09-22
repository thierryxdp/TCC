def maiores(lista, n):
    lista = list(filter(lambda x: x > n, lista))
    lista.sort()
    return lista