def conta_numero(numero, matriz):
    i = 0
    qtde = 0
    for i in range(len(matriz[i])):
        if i == numero:
            i += 1
            qtde += 1
    return qtde