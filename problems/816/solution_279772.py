def maiores(lista, n):
	lista2 = []
    for x in range(len(lista)):
		if(lista[x] > n):
			lista2.append(lista[x])

	lista2.sort()
	return lista2