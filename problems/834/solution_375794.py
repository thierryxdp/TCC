def media_matriz(matriz):
    a=0
    for c in range(len(matriz)):
        for i in range(len(matriz[c])):
            a+=matriz[c][i]
    return round(a/(len(matriz)*len(matriz[0])),2)