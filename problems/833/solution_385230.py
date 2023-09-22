def conta_numero(n, m):
    '''
    A função retorna quatas vezes um número inteiro
    aparece em uma matriz de inteiros
    int, matriz --> int
    '''
    for i in len(m):
        for j in len(m[0]):
            c = 0
            if n == m[i][j]:
                c += 1
    return c