def conta_numero(numero, matriz):
    ocorrencias = 0
    nlin = len(matriz)
    ncol = len(matriz[0])
    for x in range(nlin):
        for y in range(ncol):
            if matriz[x][y] == numero:
                ocorrencias = ocorrencias + 1
    return ocorrencias