def conta_numero(numero,matriz):
    quant = 0
    i = 0
    for i in matriz:
        for j in i:
            if numero == j:
                quant += 1
        i += 1
    return quant