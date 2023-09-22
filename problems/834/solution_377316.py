def media_matriz(matriz):
    if matriz==[] and numero==0:
                return 0
    linhas=len(matriz)
    colunas=len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
             matriz[i][j]+=matriz[i][j]
             	media=matriz[i][j]/(linhas*colunas)
    return media