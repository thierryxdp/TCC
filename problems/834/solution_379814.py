def media_matriz(matriz):
    medias = []
    for elementos in matriz:
        for number in elementos:
            media = media + float(number/2)
    return media