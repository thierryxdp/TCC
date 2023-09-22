def conta_numero(numero, matriz):
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            contador = contador + 1
            if matriz[i][j] == numero:
                contador = contador + 1
    return contador