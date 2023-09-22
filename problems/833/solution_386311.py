def conta_numero(numero,matriz):
    """"""
    qtd=0
    linhas=len(matriz)
    colunas=len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j]==numero:
                qtd=qtd+1
                else:
                    return 0
    return qtd