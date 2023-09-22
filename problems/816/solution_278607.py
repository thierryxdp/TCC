def maiores(lista, n):
    listamaior = []

    for i in lista:
        if i >= n:
            listamaior.append(i)

    return listamaior