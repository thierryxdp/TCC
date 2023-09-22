def melhor_volta(matriz):
	i = 0
	j = 0
	menor = matriz[0][0]
	for i in range(0,6):
        for j in range(0,10):
            if matriz[i][j] < menor:
                menor = matriz[i][j]
                j += 1
            else:
                j += 1
            i += 1
    
    resultado = (i,j,menor)
    return resultado