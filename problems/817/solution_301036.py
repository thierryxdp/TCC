def acima_da_media(lista):
	'''Esta função recebe uma lista de notas e retorna a lista ordenada
    com as notas acima da media.
	list >>>> list'''
    
	media = int(sum(lista) / len(lista))
	return maiores(lista, media)