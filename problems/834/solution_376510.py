def media_matriz(matriz):
    media = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            media = media + matriz[i][j]
    return media