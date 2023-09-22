def media_matriz(matriz):
    x = 0
    for i in matriz:
        for j in i:
            x = x + j
    y = len(matriz)*len(matriz[0])    
    return range(2, x/y)