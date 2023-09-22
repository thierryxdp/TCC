def media_matriz(matriz):
    elen = []
    soma = 0
    for i in range(len(matriz)):
        for j in range (matriz[i]):
            if matriz[i][j] != 0:
                elen += matriz[i][j]
    for z in range(len(elen)):
        soma += elen[s]
    med  = soma/len(elen)
        return med