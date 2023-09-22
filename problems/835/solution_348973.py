def melhor_volta(matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    C = []
    for i in range(nlin):
        for j in range(ncol):
            C.append(matriz)
            menor = min(C)
            if matriz[i][j] == menor:
                return C