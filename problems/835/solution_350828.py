def melhor_volta(matriz):

	placar = (0,0,0)
    
	for l in range(6):
		for c in range(10):
    		if matriz[l][c] < placar[1]:
				resultado = (l,matriz[l][c],c)
                
    return resultado