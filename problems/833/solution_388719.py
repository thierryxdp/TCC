def conta_numero(numero, matriz):
    c =0
    for i in range(len(matriz)):
    	for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                c=+1
    return c