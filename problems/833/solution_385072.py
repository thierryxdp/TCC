def conta_numero(numero, matriz):
    """..."""
    cont = 0
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz)):
            if matriz[i][j] == numero:
                cont += 1
    return cont