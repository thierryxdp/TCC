def media_matriz(matriz):
	'''Função que dado uma matriz de numeros inteiros e não vazia, retorna a media de todos os numeros da matriz'''
	''' list -> float'''
	numeros = 0
	divisor = 0
	i = 0
	j = 0
	while i < len(matriz):
		while j < len(matriz[i]):
			numeros += j
			divisor += 1
			j += 1
		i += 1
	return round(numeros / divisor, 2)