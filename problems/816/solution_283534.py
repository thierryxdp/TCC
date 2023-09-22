def maiores(lista,n):
    maiores=list()
    for c in lista:
        if c >= n:
            maiores.append(c)
            lista.sort()
    return maiores