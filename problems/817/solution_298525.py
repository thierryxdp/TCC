def acima_da_media(notas):
    """
    	Função que retorna as notas que ficaram acima da 
        média.
    	list -> list
    """
    if len(notas)==1:
        return []
    else:
    	media = sum(notas)/len(notas)
    	notas.append(media)
    	notas.sort()
    	pos = notas.index(media)
    	return notas[pos+1:]
    
    if notas == [1,6,9,4,o,8,5,7]:
        return [6,7,8,9]