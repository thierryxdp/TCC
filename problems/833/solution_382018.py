def conta_numero(numero,matriz):
	''' '''
	for l in matriz:
		qtd = 0
		for n in l:
			if n == numero:
				qtd = qtd + 1
	return qtd