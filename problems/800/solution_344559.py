def total(lista, dicio):

	valor = 0

	i = 0
	while i<len(lista):
		valor += dicio[lista[i]]
		i += 1

	return round(valor, 2)