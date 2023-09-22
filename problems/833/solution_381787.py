def conta_numero(matriz,elemento):
    n=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==elemento:
                n=n+1
    return n