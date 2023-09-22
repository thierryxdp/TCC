def conta_numero(numero,matriz):
    '''conta e retorna quantas vezes o numero aparece na matriz
    int,list -> int'''
    repeticoes=0
    nlin=len(matriz)
    ncol=len(matriz[])
    for i in range(nlin):
        for j in range(ncol):
            if matriz[i][j]==numero:
                repeticoes=repeticoes+1
    return repeticoes