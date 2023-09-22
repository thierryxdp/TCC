def insere(lista_numero,n):
	""" Esta função insere e ordena um numero em uma lista
	list, int -> list """
	#adiciona o numero solto a lista
	list.append(lista_numero,n)
	#ordena a lista
	list.sort(lista_numero)

	return lista_numero