def conta_numero(numero, matriz):
	'''Recebe um numero inteiro (numero) e 
    retorna quantas vezes aquele numero aparece
    na matriz
	
    int, list -> int
    '''
	
    total = 0
	for item in matriz:
		for item2 in item:
			if item2 == numero:
				total += 1

	return total