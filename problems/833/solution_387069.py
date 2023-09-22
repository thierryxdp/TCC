def conta_numero(numero,matriz):
    contador = 0
    for i in matriz:
        for j in matriz[i]:
            if matriz[i][j] ==  numero:
                contador += 1
    return contador