def maiores(lista, n):
    lista.sort()
    return [x for x in lista if x > n]