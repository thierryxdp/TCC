def repetidos(lista):
	"""."""

	lista.sort()
	i = 0
	n = 1 
	while i < len(lista):
		if lista[i] == lista[n]:
			i += 1
			n += 1
	return i