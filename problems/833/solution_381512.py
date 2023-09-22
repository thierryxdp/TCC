def conta_numero(numero,matriz):
	linhas=len(matriz)
	colunas=len(matriz[0])
	ocorrencia = 0
    for i in range(linhas):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                ocorrencia = ocorrencia + 1
    return ocorrencia