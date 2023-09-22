def maiores(lista,n):
    if min(lista)<=n:
    	lista=list.remove(lista,min(lista))
    elif min(lista)<=n:
    	continue
    elif min(lista)>n:
    	lista=list.sort(lista)
    return lista