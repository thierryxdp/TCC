def conta_numero(numero,matriz):
    contador = 0
    for i in m:
        for j in m:
            if matriz[i][j] == numero:
                contador = contador + 1
    return contador