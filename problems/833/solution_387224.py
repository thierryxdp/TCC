def conta_numeros(numero,matriz):
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            if matriz[x][y] == numero:
                return numero