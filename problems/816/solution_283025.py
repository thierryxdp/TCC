def maiores(lista, n):
	lista.append(n)
	lista.sort()
	return lista[lista.index(n)+lista.count(n):]