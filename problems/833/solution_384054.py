def conta_numero(n,matriz):
    v=0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j]==n:
                v=v+1
	return v