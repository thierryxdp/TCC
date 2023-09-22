def conta_numero(numero,matriz):
    contador=0
    for i in matriz:
        for j in matriz:
            if matriz[i][j]==numero:
                contador=contador+numero
    return contador