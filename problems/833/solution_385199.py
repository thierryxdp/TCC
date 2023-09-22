def conta_numero(numero, matriz):
    conta = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                numero += 1
    return conta