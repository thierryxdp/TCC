def conta_numero(numero,matriz):
    linha=len(matriz)
    coluna=len(matriz[0])
    quant = 0
    for i in linha:
        for j in coluna:
            if matriz[i][j] == numero:
                quant+=1
    return quant