def media_matriz(m):
    '''
    A função retorna a media de números de uma matriz
    inteira e não nula
    matriz --> int
    '''
    c = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            c += m[i][j]
    return c / (len(m) * len(m[0])