def maiores(lista,n):
    y = lista
    for i in range(len(lista)):
        if lista[i]<n:
            del lista[i]             
    	return lista.sort()