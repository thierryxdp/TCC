def maiores(lis, n):
    maiores_numeros = list()
    for i in lis:
        if i >= n:
            maiores_numeros.append(i)
    return maiores_numeros