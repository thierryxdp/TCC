def melhor_volta(matriz):
    nlin=len(matriz)
    ncol=len(matriz[0])
    menor_tempo=0
    for i in range(nlin):
        for j in range(ncol):
            menor_tempo+=min[i][j]
        return menor_tempo