def maiores(lis, n):
    maiores_numeros = list()
    for c in lis:
        if c >= n:
            maiores_numeros.append(c)
            n = len(L)
    for i in range(n-1, 0, -1):
        for j in range(0,i):
            if L[j] > L[j+1]:
                troca(L, j, j+1)

    return maiores_numeros