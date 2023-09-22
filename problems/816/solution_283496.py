def maiores(lis, n):
    maiores_numeros = list()
    numeros.sort()  # Crescente
    for c in lis:
        if c >= n:
            maiores_numeros.append(c)
    return maiores_numeros