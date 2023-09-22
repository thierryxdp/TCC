def media_matriz(matriz):
    x = 0
    for y in matriz:
        for k in y:
            x = x + k
    media = x/((len(matriz)+1)*(len(matriz[0])+1))
    media = round(media,2)
    return media