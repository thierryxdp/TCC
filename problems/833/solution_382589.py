def conta_numero(numero,matriz):
    quant = 0
    for i in len(matriz):
        if numero in matriz[i]:
            quant += 1
    return quant