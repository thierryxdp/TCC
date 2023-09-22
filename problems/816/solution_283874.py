def maiores(lista,n):
	maiores=list()
	lista.sort()
	for c in lista:
		if c >= n:
			maiores.append(c)
	return maiores