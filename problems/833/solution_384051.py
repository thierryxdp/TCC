def conta_numero(numero,matriz):
    v=0
    for i in len(matriz[0]):
        for j in range(matriz):
        	if matriz[i][j]==numero:
            	v=v+1
    return v