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
    
    return notas[pos+1:]
	if len(notas)==0:
        return []