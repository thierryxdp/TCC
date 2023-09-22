def acima_da_media(lista):
	"""Retorna uma lista ordenada com as notas que ficaram acima da média
       list --> list"""
    newLista = lista[0]
    newLista = lista[0][0] + lista[0][1]   
    if newLista >= 7:
        return newLista
    else:
        return "olá"