def media_matriz(matriz):
    media = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            media = media + numeros[i][j]
    m = media/len(matriz)
    return m