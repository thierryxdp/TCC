def conta_numero(numero,matriz):
    quant = 0
    i = 0
    j = 0
    for i in range(len(matriz)):
        for j in matriz[i]:
            if numero in matriz[i]:
                quant = quant + 1
    return quant