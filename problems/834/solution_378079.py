def media_matriz(matriz):
	""" Dada uma matriz, retorna a média de todos os números dela.
	list -> float
	"""
	count, dividendo = 0, 0
    for i in range(len(matriz)):
		for j in matriz[i]:
			dividendo += j
			count += 1
	return round(dividendo / count, 2)