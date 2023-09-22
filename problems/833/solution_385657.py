def conta_numero(numero,matriz):
    qnt = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                qnt = qnt + 1
    return qnt