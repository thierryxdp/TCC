def conta_numero(numero, matriz):
    c = 0 
    for c in range(len(matriz)): 
        c = c + 1 
        for i in range(len(matriz)):
            c = list.count(matriz[c], numero)
    	return c