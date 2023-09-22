def acima_da_media(lista):
    """
    	Retorna uma lista ordenada com as notas que ficaram acima da média.
        list -> list
    """
    media=sum(lista)/len(lista)
    lista.append(media)
    lista.sort()
    lista=lista[lista.index(media)+1:]
    posicao_media=lista.index(media)
    posicao_1dps_media=posicao_media+1
    if lista[posicao_media]==lista[posicao_1dps_media]
       lista=lista=lista[lista.index(media)+2:]
	return lista