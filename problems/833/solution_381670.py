def conta_numero(numero, matriz):
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            if matriz[i][j]==0:
                numero = numero+1
    return numero