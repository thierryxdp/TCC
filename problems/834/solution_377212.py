def media_matriz(matriz):
    media = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            media += matriz[i][j]
    return media/(len(matriz)*len(matriz[0]))