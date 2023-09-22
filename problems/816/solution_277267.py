def maiores(lista,n):
	"""Função em que dada uma lista de números inteiros e um número inteiro n retorna outra lista que contem todos os números inteiros da lista original maiores que n.
	list -> list"""
	list.insert(lista,0,n)
	list.sort(lista)
	local=list.index(lista,n)
	return lista[local+1:]