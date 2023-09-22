def acima_da_media(notas):
    """
    	Função que retorna as notas que ficaram acima da 
        média.
    	list -> list
	"""
    media = sum(notas)/len(notas)
    if len(notas)==1:
        return []
    if media in notas:
        posi = notas.index(media) 
        return notas[posi:]
    else:
    	notas.append(media)
    	notas.sort()
    	pos = notas.index(media)
    	return notas[pos+1:]