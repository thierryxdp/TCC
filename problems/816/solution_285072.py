def maiores(lista, n):
    '''Função que dada uma lista de números e um inteiro n, retorna uma lista ordenada contendo os números da lista original maiores que n.
    list, int -> list'''
    lista2 = list.append(lista,n)
	lista2 = list.sort(lista2)
    return lista2[lista2[n]:]