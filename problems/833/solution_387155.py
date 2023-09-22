def conta_numero(numero,matriz):
    contador = 0
    for i in range(matriz):
        for j in range(matriz[i]):
            if matriz[i][j]==numero:
                contador += 1
    return contador