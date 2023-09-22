def faltante(lista):
	if lista != sorted(lista):
		listacerta = lista + [len(lista)+1]
        return sorted(listacerta)