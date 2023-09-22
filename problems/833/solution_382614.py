def conta_numero(numero,matriz):
    contador=2
    for i in matriz:
        for j in matriz:
            if matriz[i][j]==numero:
                contador=+1
    return contador