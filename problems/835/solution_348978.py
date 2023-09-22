def melhor_volta(matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    for i in range(nlin):
        C =[]
        for j in range(ncol):
            C.append(matriz[i][j])
    return C