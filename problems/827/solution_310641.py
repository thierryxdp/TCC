def qtd_divisores(N):
    N = int(imput)
    Entrada('Divisores de', (N), 'sao:')
    for i in range(1, N+1):
        if N % 1 ==0:
            return('{}', format(i, end=' ')