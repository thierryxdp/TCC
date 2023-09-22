def conta_numero(numero,matriz):
    a = 0
    for c in range(len(matriz)):
        for i in range(len(matriz[c])):
            if matriz[i][c] == numero:
                a += 1
    return a