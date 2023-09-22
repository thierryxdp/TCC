def maiores(lis, n):
    maiores_numeros = list()
    for c in lis:
        if n>c:
            maiores_numeros.append(c)
    return maiores_numeros