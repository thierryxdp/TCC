def faltante(lista):
    """funcao que dada uma lista com numeros de 1 a n indica qual numero esta faltando na lista"""
	"""list->int"""
    indice = 0
    tamanho = 0
    while indice < tamanho:
        if indice + 1 != lista[indice]:
            return indice + 1