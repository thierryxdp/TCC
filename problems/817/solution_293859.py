def acima_da_media(lista):
    """Funcao que retorna uma list ordenada com as notas que ficaram acima da media;
    list -> list"""
    
    list.sort(lista)
    ntermos = sum(lista)
    qtermos = len(lista)
    position = ntermos//qtermos
    
    
    if media in lista:
        v1 = list.index(lista, position)
    	p = v1+1
        return lista[p:]
    else:
        list.append(lista, media)
    	list.sort(lista)
    	v1 = list.index(lista, media)
    	p = v1+1
    
    	return lista[p:]