def conta_numero(numero, matriz):
    for c in range(10):
    	for i in range(len(matriz)):
        	c = list.count(matriz[c], numero)
    return c