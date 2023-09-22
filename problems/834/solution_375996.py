def media_matriz(matriz):
    Media=0
    for i in range(len(matriz)):
        for c in range(len(matriz[0])):
            Media=Media+matriz[i][c]
    return round(Media/(len(matriz)*len(matriz[0])),2)