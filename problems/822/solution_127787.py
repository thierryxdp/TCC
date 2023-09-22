def repetidos(lista):
	"""."""

	lista.sort()
	i = 0
	n = list.set(lista)
	while i < len(lista):
		if lista[i] not in n :
			i += 1
	return i