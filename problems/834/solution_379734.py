def media_matriz(matriz):
    soma=[]
    nlin=len(matriz)
    ncol=len(matriz[0])
    for i in range(nlin):
        for j in range(ncol):
            soma=linha[i][j]+matriz[i][j]
        return soma