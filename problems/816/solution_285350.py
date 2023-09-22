def maiores(lista,n):
	lista=list.sort(lista)             
    k=0
    if lista[k]<=n:
    	k=k+1
    elif lista[k]>n:
    	lista= del lista[k:]
    return lista