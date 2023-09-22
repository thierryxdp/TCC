def media_matriz(matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    for i in range(nlin):
        for j in range(ncol):
            x = sum(i) + sum(j)/len(matriz)
    return x