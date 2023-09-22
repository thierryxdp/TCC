def repetidos(lista):
	"""."""

	lista.sort()
	i = 0
	
	while i < len(lista):
		if lista[i] not in list.set(lista):
			i += 1
	return i