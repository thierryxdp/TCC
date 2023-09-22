def media_matriz(matriz):
	""" 
	"""
	count, dividendo = 0, 0
    for i in range(len(matriz)):
		for j in matriz[i]:
			dividendo += j
			count += 1
	return round(dividendo / count, 2)