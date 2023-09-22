def conta_numero(numero,matriz):
    v=0
    for i in range(matriz):
        for j in range(matriz):
        	if matriz[i][j]==numero:
            	v=v+1
    return v