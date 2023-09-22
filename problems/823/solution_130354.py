def faltante(lista):
	"""Função que dada uma lista com N − 1 inteiros numerados de 1 a N,
	descubra qual número inteiro deste intervalo está faltando.
	lista -> int.
	"""
	tamanho = len(lista)+1
	lista_completa = []
	corrente = 1
	i = 0
	resposta = 0
	while corrente <= tamanho:
		lista_completa += [corrente]
		corrente += 1
	while i < tamanho:
		if lista_completa [i] not in lista:
			resposta += lista_completa[i]
		i += 1
	return resposta