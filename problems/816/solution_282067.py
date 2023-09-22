def maiores(lista,n):
    list.sort(lista)
    for i in lista:
    	if lista[i] < n:
        	list.remove(lista,i)
    
    return lista