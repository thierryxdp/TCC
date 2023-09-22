def maiores(lista_inteiros,n):
	"""Função na qual dada uma lista de valores inteiros,
           e um valor inteiro n, retorna uma outra lista com todos os valores
           da lista original maiores que n"""
	colocando = list.append(lista_inteiros,n)
	list.sort(lista_inteiros)
	posicao = list.index(lista_inteiros,n)
	return lista_inteiros[posicao+1:]