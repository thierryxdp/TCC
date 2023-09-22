def media_matriz(matriz):
    soma=0
    for i in (len(matriz)):
        for j in (len(matriz[0])):
                soma+=matriz[i][j]
    return soma