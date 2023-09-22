def conta_numero(numero,matriz):
    quant = 0
    for i in len(matriz):
        for j in len(matriz[0]):
            if matriz[i][j] == numero:
                quant+=1
    return quant