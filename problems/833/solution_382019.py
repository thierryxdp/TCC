def conta_numero(numero,matriz):
	''' '''
    qtd = 0
	for l in matriz:
		for n in l:
			if n == numero:
				qtd = qtd + 1
	return qtd