def conta_numero(numero,matriz):
    if matriz != []:
        linha=range(len(matriz))
        coluna=range(len(matriz[0]))
        quant = 0
        for i in linha:
            for j in coluna:
                if matriz[i][j] == numero:
                    quant+=1
        return quant
    else:
        return 0