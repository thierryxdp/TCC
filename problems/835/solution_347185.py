def melhor_volta(matriz):
    
	menor = matriz[0][1]
	for i in range(0,6):
        for j in matriz[i]:
            if j <= menor:
                menor = j
                j += 1
            else:
                j += 1
       	 i += 1
    
    resultado = (i,menor,j)
    return resultado