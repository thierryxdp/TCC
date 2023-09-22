def media_matriz(matriz):
    d = 0
    n=0
    i=0
    j=0
    for i in matriz:
        for j in matriz:
            n += j
            d += 1
    return round(n/j, 2)