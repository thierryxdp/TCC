def acima_da_media(lista,media):
    """funcao que retorna os numeros de uma lista dada maior que de uma determinada media;lista->lista"""
	list.insert(lista,0,media)
    list.sort(lista)
    posicao=list.index(lista,media)
    return lista[(posicao+1):]