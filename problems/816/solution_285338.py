def maiores(lista,n):
    if min(lista)<=n:
    	lista=list.remove(lista,min(lista))
    	if min(lista)<=n:
    	continue
        else:
    		lista=list.sort(lista)
    return lista