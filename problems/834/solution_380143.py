def media_matriz(matriz):
    ''' retorna a media da matriz
    list(list) -> int'''
    media = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            media += matriz[i][j]
    return media