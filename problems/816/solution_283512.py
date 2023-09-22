def maiores(lis, n):
    maiores_numeros = list()
    lis.sort(maiores_numeros)
    for c in lis:
        if c >= n:
            maiores_numeros.append(c)
    return maiores_numeros