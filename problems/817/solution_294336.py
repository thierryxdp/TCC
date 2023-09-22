def acima_da_media(lista):
    '''Funcao que retorna uma lista com todas as notas acima da media.
list->list'''
    media=sum(lista)//len(lista)
    if media in lista:
        list.sort(lista)
    	y=list.index(lista,media)
    	return lista[y+1:]
    else:
        list.append(lista,media)
   	    list.sort(lista)
    	z=list.index(lista,media)
    	return lista[z+1:]