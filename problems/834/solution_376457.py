def media_matriz(m):
    '''Dada uma matriz, a função retorna a média dos números
       da matriz
       list -> float
       Parametros:
       m: matriz a ser digitada'''
    col = len(m[0])
    soma = 0
    l = []
    for c in range(0, len(m)):
        for p in range(0, col):
            soma += int(m[c][p])
    media = soma / (len(m) * len(m[0]))
    return roun(media, 2)