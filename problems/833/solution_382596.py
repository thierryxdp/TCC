def conta_numero(numero,matriz):
    quant = 0
    i = 0
    for i in range(len(matriz)):
        if numero in matriz[i][i]:
            quant = quant + 1
    return quant