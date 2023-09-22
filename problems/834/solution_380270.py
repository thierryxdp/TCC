def media_matriz(matriz):
    i = 0
    t = 0
    media = 0
    if matriz != []:
        for lin in range(0, len(matriz)):
            for col in range(0, len(matriz[lin])):
                t += 1
                i += matriz[lin][col]
                media = i / t

    return round(media, 2)