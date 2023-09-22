def insere(lista_numero, n):
	"""Função que insere um número inteiro n em uma lista ordenada sem alterar sua ordem
	lista, int -> lista"""
	
	lista_final = lista_numero + [n]
	lista_final.sort()
	
	return lista_final