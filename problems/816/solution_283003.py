def maiores(lista, n):
	if n not in lista:
		lista.append(n)
	lista.sort()
	return lista[lista.index(n)+1:]