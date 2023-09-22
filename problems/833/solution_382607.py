def conta_numero(numero,matriz):
    contador=0
    for i in len(matriz):
        for j in len(matriz):
            if matriz[i][j]==numero:
                contador=contador+1
    return contador