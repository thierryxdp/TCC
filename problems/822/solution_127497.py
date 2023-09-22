def repetidos(lista):
	"""."""

	lista.sort()
	i = 0
	
	while i < range(len(lista)-1):
		if lista[i] == lista[i+1]:
			i += 1
	return i