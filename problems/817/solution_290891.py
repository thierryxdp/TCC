def acima_da_media(lista):
    a=(sum(lista))/(len(lista))
    if list.count(lista,a)>0:
        list.insert(lista,0,a)
        list.sort(lista)
    	return lista[list.index(lista,a)+2:]
    else:
    	list.insert(lista,0,a)
    	list.sort(lista)
    	return lista[list.index(lista,a)+1:]