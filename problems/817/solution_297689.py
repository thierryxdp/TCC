def acima_da_media(numeros):
	x = sum(numeros)/len(numeros)
	list.sort(numeros)
	y =list.index(numeros,x)
	return numeros[y+1:]