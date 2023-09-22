def conta_numero(numero,matriz):
    k=0
    for i in len(matriz):
        for j in len(matriz[0]):
            if matriz[i][j]==numero:
                k=k+1
    return k