def conta_numero(numero,matriz):
	linhas=len(matriz)
	colunas=len(matriz[0])
	ocorrencias=[]
	for numero in range(linhas):
		qtd=0
		for num in range(colunas):
			if num==numero:
				qtd=qtd+1
		list.append(ocorrencias, qtd)
	return ocorrencias