def filtra_pares(lista):
    """filtra os elementos pares de uma lista"""
    lista1 = list(lista)
	return filter(lambda x: x % 2 == 0, lista1)