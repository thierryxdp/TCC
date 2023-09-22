def maiores(lista,n):
    if min(lista)<=n:
    	lista=list.remove(lista,min(lista))
    else:
        lista=list.sort(lista)
    	if min(lista)<=n:
    		lista=list.remove(lista,min(lista))
    	else:
        	lista=list.sort(lista)
       		if min(lista)<=n:
    			lista=list.remove(lista,min(lista))
    		else:
        		lista=list.sort(lista)
    return lista