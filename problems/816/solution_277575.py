def maiores(lista, n):
	'''Dada uma lista de n ́umeros inteiros e um n ́umero inteiro n, retorna
    outra lista, que contenha todos os n ́umeros da lista original maiores 
    que n. lista,int -> lista'''
	if n not in lista:
		list.append(lista,n)
		list.sort(lista)
		pos = list.index(lista,n)
		return lista[pos+1:]
	else:
		list.sort(lista)
		pos = list.index(lista,n)
		return lista[pos+1:]