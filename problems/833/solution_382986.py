def conta_numero(numero,matriz):
    vezes = 0
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            if matriz[x][y]==numero:
                vezes += 1
    return vezes