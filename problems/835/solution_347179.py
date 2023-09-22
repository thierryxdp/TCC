def melhor_volta(matriz):
    
	menor = matriz[0][1]
	for t in matriz[i]:
        for j in len(matriz):
            if matriz[i][j] <= menor:
                menor = matriz[i][j]
                j += 1
            else:
                j += 1
       	 i += 1
    
    resultado = (i,j,menor)
    return resultado