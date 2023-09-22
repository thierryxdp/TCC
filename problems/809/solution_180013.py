def intercala(lista1, lista2):
	'''
dado duas listas com 3 elementos cada como argumento,
retorna uma terceira lista com todos os elementos das
duas primeiras intercaladas
dados de entrada: list, list
dados de retorno: list
	'''
    concatenacao = lista1 + lista2
	return [concatenacao[0], concatenacao[3], concatenacao[1], concatenacao[4], concatenacao[2], concatenacao[5]]