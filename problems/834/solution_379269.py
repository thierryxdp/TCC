def media_matriz(matriz):
    cont = 0
    div = len(matriz)*len(matriz[0])
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            cont= cont + matriz[i][j]
    R=cont/div
    return round(R, 2)