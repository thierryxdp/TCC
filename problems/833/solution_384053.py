def conta_numero(n,m):
    v=0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j]==numero:
                v=v+1
	return v