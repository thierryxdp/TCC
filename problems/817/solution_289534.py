def acima_da_media(lista):
    media=sum(lista)/len(lista)
    if media in lista:
        lista1=list.index(lista,media)
        return lista(lista[lista1+1:]
    else:
 		list.append(lista,media)
    	list.sort(lista)
    	lista1=lista.index(media)
    	return lista[lista1+1:]