def conta_numero(num, matriz):
	'''Conta quantas vezes um número aparece em uma 
    matriz
    	int, list -> int'''
	vezes = 0
	for i in matriz:
		for j in i:
			if num == j:
				vezes += 1
	return vezes