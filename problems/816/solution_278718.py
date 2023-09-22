def maiores(lista_inteiros,n):
	"""Função na qual dada uma lista de valores inteiros,
           e um valor inteiro n, retorna uma outra lista com todos os valores
           da lista original maiores que n"""
	if n in lista_inteiros:
		posicao = lista_inteiros.index(n)
		remocao = list.remove(lista_inteiros,n)
		colocando = list.append(lista_inteiros,n)
		organizando = list.sort(lista_inteiros)
		maiores_n = lista_inteiros[n:]
		return maiores_n
	elif n not in lista_inteiros:
		inserindo = list.append(lista_inteiros,n)
		organizando = list.sort(lista_inteiros)
		maiores_n = lista_inteiros[n:]
		return maiores_n