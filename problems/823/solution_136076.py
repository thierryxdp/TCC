def faltante(lista):
	i = 1
	lista.sort()
	while i < len(lista):
		if(lista[i]-lista[i-1] > 1):
			return lista[i-1]+1
		i = i+1
	if 1 in lista:
		return len(lista)+1
	else:
		return 1