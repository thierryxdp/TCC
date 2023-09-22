def conta_numero(numero,matriz):
    contador = o
    for i in matriz:
        for j in matriz[i]:
            if matriz[i][j] ==  numero:
                contador += 1
    return contador