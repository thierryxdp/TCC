def conta_numero(numero, matriz):

    acumulador = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero == matriz[i][j]:
                acumulador += 1
    return acumulador