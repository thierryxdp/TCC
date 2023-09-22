def acima_da_media(lista):
    ''' '''
    lista_medias=[]
    for i in lista:
        if i > 4:
            lista_medias.append(i)
            lista_medias.sort()    
		return lista_medias
    	
    else:
    	return []