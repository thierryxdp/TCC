def conta_numero(numero,matriz):
    qtd=0
    linhas=len(matriz)
    coluna=len(matriz[0])
    for i in range(linhas):
        for j in range(coluna):
            if matriz[i][j]=numero:
                qtd=qtd+1
                return qtd