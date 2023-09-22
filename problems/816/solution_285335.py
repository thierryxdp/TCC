def maiores(lista,n):
    if min(lista)<=n:
    	list.remove(lista,min(lista))
    	while min(lista)<=n:
            continue
    elif min(lista)>n:
    	lista=list.sort(lista)
    return lista