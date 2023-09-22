def conta_numero(numero,matriz):
    s = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                s += 1
            else:
                s += 0
    return s