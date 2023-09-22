def conta_numero(n, m):
    '''
    A função retorna quatas vezes um número inteiro
    aparece em uma matriz de inteiros
    int, matriz --> int
    '''
    c = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if n == m[i][j]:
                c += 1
    return c