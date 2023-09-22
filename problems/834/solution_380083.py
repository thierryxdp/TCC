def media_matriz(matriz):
    '''retorna a media de todos os numeros de uma matriz
    matriz->float'''
    a=0
    b=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            a+=matriz[i][j]
            b+=1
    return round(a/b,2)