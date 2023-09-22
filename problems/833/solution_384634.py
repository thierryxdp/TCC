def conta_numero(numero, matriz):
    contador=0
    m=len(matriz)
    for i in range(m):
        for j in range(m[i]):
            if matriz[i][j] == numero:
                contador=contador+1
    return contador