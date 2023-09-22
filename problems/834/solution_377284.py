def media_matriz(matriz):
    total = 0
    for x in matriz:
        for y in range(len(x)):
            total += x[y]
    media = total/(len(matriz)*len(matriz[y]))
    return media.round(2)