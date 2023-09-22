def conta_numero(numero, matriz):
	contador = 0
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if matriz[i][j] == numero:
                contador += 1

    return contador