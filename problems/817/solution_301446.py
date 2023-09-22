def acima_da_media(lista):
	'''Esta função recebe uma lista e retorna a lista ordenada
	list -> list'''
    
	media = int(sum(lista) / len(lista))
	return maiores(lista, media)