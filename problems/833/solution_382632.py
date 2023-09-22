def conta_numero(numero,matriz):
    quant = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero == matriz[i][j]:
                quant = quant + 1
    return quant