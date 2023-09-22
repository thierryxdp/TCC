def maiores(lista,n):
    y = lista
    for i in range(len(lista)+1):
        if lista[i]<n:
            del lista[i]             
    		return lista