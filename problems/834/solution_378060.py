matrf media_matriz(matriz):
	'''Função que dado uma matriz de numeros inteiros e não vazia, retorna a media de todos os numeros da matriz'''
	''' list -> float'''
	lista = []
	for i in matriz:
		lista += i
	return round((sum(lista) / len(lista)), 2)