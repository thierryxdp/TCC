def conta_numero(numero, matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            m = matriz[i][j]
            c = sum(x.count(numero) for x in m))
           	return c