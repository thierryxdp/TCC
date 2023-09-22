def melhor_volta(matriz):
    
	menor = matriz[0][1]
	for i in range(0,6):
        for j in matriz[i]:
            if j <= menor:
                menor = matriz[i][j]
                j += 1
            else:
                j += 1
       	 i += 1
    
    resultado = (i,j,menor)
    return resultado