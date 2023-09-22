def maiores(lista, n):
    for x in lista:
        if x > n:
            lista.append(x)
    return lista.sort()