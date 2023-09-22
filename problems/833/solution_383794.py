def conta_numero(numero,matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    count = 0
    for i in range(nlin):
        for j in range(ncol):
            if matriz[i][j] == numero:
            count = count + 1
    return count