def media_matriz(matriz):
    v=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            v=v+matriz[i][j]
    return v