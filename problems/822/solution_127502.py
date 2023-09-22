def repetidos(lista):
	"""."""

	lista.sort()
	i = 0
	
	while i < len(lista):
		if lista[i] == range(len(lista)-1):
			i += 1
	return i