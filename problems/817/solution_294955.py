def acima_da_media(lista):
    media = sum(lista)/len(lista)
    x = list.count(lista, media)
    if(x>0)
    	return lista[list.index(lista, media)+1:]
    else:
        list.append(lista, media)
    	list.sort(lista)
    	return lista[list.index(lista, media)+1:]