def media_matriz(matriz):
    """Determina a média dos elementos de uma matriz"""
    media = 0
    m = len(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            elemento = matriz[i][j]
            media += elemento
    return round(media/(int(m)*int(len(matriz[0],2))))