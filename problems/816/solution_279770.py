def maiores(lista, n):
	lista2 = []
    for x in range(len(lista)):
		if(x > n):
			lista2.append(x)

	lista2.sort()
	return lista2