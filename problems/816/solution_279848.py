def maiores(lista,n):
	"""Função que retorna outra lista com os números da lista dada como parâmetro maiores que o inteiro n
	lista, int -> lista"""
	
	lista_ordenada = lista + [n]
	lista_ordenada.sort()
	indice = lista_ordenada.index(n)
	
	return lista_ordenada[indice + 1:]