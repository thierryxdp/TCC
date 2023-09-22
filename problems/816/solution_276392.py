def maiores(lista,n):
	'''Função que dada uma lista de números inteiros e um número inteiro n, retorna outra
	lista que contém todos os números da lista original que são maiores do que o número n.
	Entrada: lista, int
	Saída: lista'''
	lista.append(n)
	list.sort(lista,reverse=True)
	localizacao=list.index(lista,n)
	lista=lista[0:localizacao]
	list.sort(lista)
	return lista