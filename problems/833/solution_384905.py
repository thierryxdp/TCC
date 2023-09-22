def conta_numero(numero, matriz):
	""" Recebe um número e uma matriz, e conta quantas vezes o número aparece na matriz.
	int, list -> int
	"""
	count = 0
	for i in range(len(matriz)):
		for j in matriz[i]:
			if j == numero:
				count += 1
	return count