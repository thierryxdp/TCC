def conta_numero(numero, matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            m = matriz[i][j]
            if numero in m:
                c = list.count(m, numero)
            	return c