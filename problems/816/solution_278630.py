def maiores(l,n):
	numeros_maiores = list()
	for x in l:
		if x >= n:
			numeros_maiores.append(x)
			list.sort(numeros_maiores)
	return numeros_maiores