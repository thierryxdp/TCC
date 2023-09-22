def acima_da_media(lista):
    	n = sum(lista)/len(lista)
    	list.insert(lista,0,n)
    	list.sort(lista)
    	x = list.index(lista,n)
    	return lista[x+1:]