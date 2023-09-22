def conta_numero(numero, matriz):
    """..."""
    cont = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if numero in matriz[i][j]:
                cont += 1
    return cont