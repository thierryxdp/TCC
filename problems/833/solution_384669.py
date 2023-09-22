def conta_numero(matriz, n):
    quant = 0
    for x in range(len(matriz)):
        if n in matriz: 
            quant = quant +1 
    return quant