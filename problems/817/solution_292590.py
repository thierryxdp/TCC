def acima_da_media(lista)
	"""Retorna uma lista ordenada com as notas que ficaram acima da média
       list --> list"""
    newLista = lista[0]
    lista[0] = sum(lista[0])
    if lista [0] >= 7:
        return newLista
    else:
        return "olá"