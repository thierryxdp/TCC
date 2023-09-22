def maiores(lista,n):
    list.extend(lista,[n])
    list.sort(lista)
    lista1 = list.index(lista,n)
    return lista[(lista1+1):]

	"""recebe uma lista e um numero n e retorna outra lista com valores
	maiores que n, list e int->list"""