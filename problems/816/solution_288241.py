def maiores(lis, n):
    maiores_numeros = list()
    for c in lis:
        if c >= n:
            maiores_numeros.sort(c)
    return maiores_numeros