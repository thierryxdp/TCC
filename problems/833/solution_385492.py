def conta_numero(numero,matriz):
    quant = 0
    i = 0
    while i < len(m):
        for j in matriz[i]:
            if numero == j:
                quant += 1
        i += 1
    return quant