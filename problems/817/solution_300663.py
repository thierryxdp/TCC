def acima_da_media(lista)
	'''Dada uma lista, retorna uma lista ordenadas
    com os valores acima da media;
    list -> list'''
    return maiores(lista, statistics.mean(lista))