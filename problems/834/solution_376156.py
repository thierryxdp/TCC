def media_matriz(matriz):
    """Determina a média dos elementos de uma matriz"""
    media = 0
    m = len(matriz)
    n = len(matriz[0])
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            elemento = matriz[i][j]
            media += elemento
    return media/int(len(matriz))*int(len(matriz[0]))