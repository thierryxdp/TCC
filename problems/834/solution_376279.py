def media_matriz(matriz):
    media = 0
    if matriz != []:
        for lin in range(0, len(matriz)):
            for col in range(0, len(matriz[lin])):
                tamanho = len(matriz[lin]) * len(matriz[lin])
                media += matriz[lin][col] / tamanho

    return round(media, 2)