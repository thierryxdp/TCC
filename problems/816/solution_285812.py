def maiores(lista_numero,n):
	""" Esta função insere e ordena todos os numeros maiores que n em ordem crescente
	list, int -> list """
	#adiciona o numero solto a lista
	list.append(lista_numero,n)
	#ordena a lista
	list.sort(lista_numero)
	#ordena os maiores 
	lista_final = lista[list.index(lista,n)+1:]

	return lista_final