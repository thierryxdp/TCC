def faltante(lista):
	i = 1
	lista.sort()
	while i < len(lista):
		if(lista[i]-lista[i-1] > 1):
			return lista[i]+1
	return 1