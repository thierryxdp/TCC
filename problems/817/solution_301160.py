def acima_da_media(lista):
    if len(lista)>1:
    	x=sum(lista)/len(lista)

     
    	list.append(lista,x)
    	list.sort(lista)
   
    	del lista[:(list.index(lista,x)+1)]
    	return lista
	else:
        return[]