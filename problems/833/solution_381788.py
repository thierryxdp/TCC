def conta_numero(numero,matriz):
    n=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                n=n+1
    return n