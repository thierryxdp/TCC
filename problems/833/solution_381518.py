def conta_numero(numero,matriz):
	if matriz==[]:
		return 0
	else:
		linhas=len(matriz)
		colunas=len(matriz[0])
		ocorrencia = 0
    	for i in range(linhas):
        	for j in range(colunas):
            	if matriz[i][j] == numero:
                	ocorrencia = ocorrencia + 1
    	return ocorrencia