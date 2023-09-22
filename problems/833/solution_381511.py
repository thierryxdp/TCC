def conta_numero(numero,matriz):
	linhas=len(matriz)
	colunas=len(matriz[0])
	ocorrencia = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                ocorrencia = ocorrencia + 1
    return ocorrencia