def acima_da_media(lista):
    """
    	Retorna uma lista ordenada com as notas que ficaram acima da média.
        list -> list
    """
    media=sum(lista)/len(lista)
    lista.append(media)
    lista.sort()
    lista=lista[lista.index(media)+1:]
	return lista