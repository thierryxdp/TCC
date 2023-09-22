def maiores(l,n):
	numeros_maiores = list()
	for x in l:
		if x >= n:
			numeros_maiores.append(x)
			list.sort(numeros_maiores)
	return numeros_maiores

def acima_da_media(lista):
	media = sum(lista)/(len(lista))
	aprovados = maiores(lista,media)
	return aprovados