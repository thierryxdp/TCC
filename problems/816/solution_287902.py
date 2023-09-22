def maiores(lista_numero,n):
	"""Função que dada uma lista de números inteiros, retorna outra lista que contenha todos os números da lista original maiores que n, em ordem crescente"""
	lista=lista_numero+[n]
    list.sort(lista)
    indice=lista.index(n)
    return lista[indice+1:]