def insere(lista_numero,n):
	"""Função em que dada uma lista ordenada e crescente de números inteiros e um número inteiro n, inclui n em uma posição da lista sem quebrar a ordem.
	list ->list"""
	list.insert(lista_numero,0,n)
	list.sort(lista_numero)
	return lista_numero