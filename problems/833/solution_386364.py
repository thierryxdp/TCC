def conta_numero(numero,matriz):
    ind=0
    if matriz==[]:
        return 0
    linhas=len(matriz)
    colunas=len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j]==numero:
                ind+=1
    return ind