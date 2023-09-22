def media_matriz(matriz):
	'''Função que dado uma matriz de numeros inteiros e não vazia, e retorna a media de todos os numeros da matriz'''
	''' list -> float'''
	lista_de_numeros = []
	for i in matriz:
		lista_de_numeros += i
	return round((sum(lista_de_numeros) / len(lista_de_numeros)), 2)