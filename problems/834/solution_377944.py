def media_matriz(matriz):
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            contador = contador + matriz[i][j]
    return contador/(len(matriz)*len(matriz[0]))