def conta_numero(numero,matriz):
    quant = 0
    i = 0
    while i < range(len(matriz)):
        if numero in matriz[i]:
            quant = quant + 1
        i = i + 1
    return quant