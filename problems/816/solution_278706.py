def maiores(lista_inteiros,n):
	"""Função na qual dada uma lista de valores inteiros,
           e um valor inteiro n, retorna uma outra lista com todos os valores
           da lista original maiores que n"""
	#Incluindo (n) na lista
	lista_inteiros.append(n)
	#Organizando a lista
	list.sort(lista_inteiros)
	#Lista com valores maiores que n
	nova_lista = lista_inteiros[n:]
	return nova_lista