def conta_numero(numero,matriz):
    repetiu = 0
    for indice in range(0, len(matriz)):
        if matriz[indice] == numero:
            repetiu += 1
        else:
            repetiu == 0
    return repetiu