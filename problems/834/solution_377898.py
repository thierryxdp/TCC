def media_matriz(matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    contador = 0
    for i in range(nlin):
        for j in range(ncol):
            contador += sum(matriz[i][j])
    return contador/(nlin)