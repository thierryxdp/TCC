def media_matriz(matriz):
    a=0
    for c in range(len(matriz)):
        for i in range(len(matriz[c])):
            a+=i
    return a/len(matriz)