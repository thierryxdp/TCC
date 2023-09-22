def conta_numero(numero, matriz):
    ''''''
    c=0
    c2=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
        	if j == numero:
            	c=c+1
    return c