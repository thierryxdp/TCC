def media_matriz(m):
    '''
    A função retorna a media de todos os números
    de umamatriz inteira não vazia
    matiz --> int
    '''
    c = 0
    for i in range(len(m)):
        for j in range(len(m)):
            c += m[i][j]
    return round(c / (len(m) * len(m[0]), 2)