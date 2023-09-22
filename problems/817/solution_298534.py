def acima_da_media(notas):
    """
    	Função que retorna as notas que ficaram acima da 
        média.
    	list -> list
	"""
    media = sum(notas)/len(notas)
    notas.append(media)
    notas.sort()
    pos = notas.index(media)
    
    if len(notas)==1:
        return []
    if media in notas:
        return notas[pos+2:]
    else:
    	notas.append(media)
    	notas.sort()
    	pos = notas.index(media)
    	return notas[pos+1:]