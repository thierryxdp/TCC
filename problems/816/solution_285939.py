def maiores(lista, n):
	''' Esta função recebe uma lista e um número inteiro e
    retorna uma lista com os numeros a partir do número inteiro
	list, int -> list'''
	if n in lista:
	list.sort (lista)
	lista1 = lista[list.index(lista, n) + 1:]
	return lista1
	else:
	lista.insert(-1, n)
	list.sort(lista)
	lista1 = lista[list.index(lista, n) + 1:]
		return lista1