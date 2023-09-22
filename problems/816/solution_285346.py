def maiores(lista,n):
	lista=list.sort(lista)             
    k=0
    while lista[k]<=n:
    	k=k+1
    if lista[k]>n:
    	lista=del lista[k]
    return lista