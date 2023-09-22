def maiores(lis, n):
    maiores_numeros = list()
     n = len(L)
    for c in lis:
        if c >= n:
            maiores_numeros.append(c)
    for i in range(n-1, 0, -1):
        for j in range(0,i):
            if lis[j] > lis[j+1]:
                troca(L, j, j+1)

    return maiores_numeros