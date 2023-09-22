def conta_numeros(numero,matriz):
    i= 0
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            if matriz[x][y] == numero:
                i+= numero
    return numero