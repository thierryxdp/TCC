def conta_numero(numero,matriz):
    quant = 0
    for i in matriz:
        i = 0
        for j in matriz[i]:
            if numero == j:
                quant += 1
    return quant