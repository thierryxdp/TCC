def media_matriz(matriz):
    lista = []
    a = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            a = matriz[i][j] + matriz[i+1][j+1]
    return a