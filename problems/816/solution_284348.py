def maiores(lista, n):
    lista.sort()
    listamaior = [x for x in lista if x > n]
    return listamaior