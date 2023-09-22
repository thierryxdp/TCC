def conta_numero(numero,matriz):
	''' '''
	ocorrencias = 0
	for l in matriz:
		qtd = 0
		for n in l:
			if n == numero:
				qtd = qtd + 1
	return qtd