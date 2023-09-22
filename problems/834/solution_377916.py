def media_matriz(matriz):
    c=0
    i=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            c=c+matriz[i][j]
            i=i+1
    return c/i