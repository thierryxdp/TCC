def media_matriz(matriz):
    media = 0
    for i in matriz:
        for j in matriz[i]:
            media += matriz[i][j]
    return media/(len(matriz)*len(matriz[0]))