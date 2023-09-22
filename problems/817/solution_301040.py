def acima_da_media(lista):
	'''Esta função recebe uma lista de notas e retorna a lista ordenada
    com as notas acima da media.
	list >>>> list'''
    
	media = int(sum(lista) / len(lista))
    if n in lista:
		list.sort(lista)
		lista1 = lista[list.index(lista, n) + 1:]
		return lista1
	else:
		lista.insert(-1, n)
		list.sort(lista)
		lista1 = lista[list.index(lista, n) + 1:]
		return lista1
	return maiores(lista, media)