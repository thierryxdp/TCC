def maiores(lista,n):
    ''''Função. que dada uma lista e um número inteiro n, retorna uma lista contendo todos os números da lista original maiores que n.'''
    ''' list, int -> list'''
	if n not in lista:
		list.append(lista,n)
	list.sort(lista)
	indice = list.index(lista,n)
	
	return lista[indice + 1 : ]