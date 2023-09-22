def maiores(lista, n):
    maiores = []
    for i in lista:
        if i > n:
            maiores += [i]
    return maiores