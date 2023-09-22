def media_matriz(matriz):
    media = 0
    if matriz != []:
        for lin in range(0, len(matriz)):
            for col in range(0, len(matriz[lin])):
                media = matriz[lin][col] / len(matriz[lin][col])

    return round(media, 2)