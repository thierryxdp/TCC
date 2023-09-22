def conta_numero(num,matriz):
	"""
		Fun¸c˜ao que dada um numero e uma matriz de inteiros, conta e
		retorna quantas vezes aquele n´umero aparece na matriz.
		"""
	count = 0
	for lista in matriz:
		for elem in lista:
			if elem == num:
				count +=1
	return count