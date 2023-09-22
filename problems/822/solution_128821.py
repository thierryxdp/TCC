def repetidos(lista):
	"""Recebe uma lista e retorna a quantidade de vezes em que um algarismo é exatamente igual
    ao elemento anterior na ordem da lista
    assinatura: lista --> int
    """
    slic=lista[1,len(lista)+1]
    return slic