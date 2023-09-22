def media_matriz(matriz):
    a = 0
    for b in matriz:
        a = a + sum(b)
    q = len(matriz)*len(matriz[0])
    return a/q