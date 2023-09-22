def media_matriz(matriz):
    media = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            media.append(matriz[i][j])
    return media