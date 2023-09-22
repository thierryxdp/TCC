def conta_numero(numero, matriz):
    ocorrencias = 0
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            if matriz[x][y] == numero:
                ocorrencias = ocorrencias + 1
    return ocorrencias