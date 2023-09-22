def maiores (lista,n):
    list.sort(lista)
    if n in lista:
    	p = list.index(lista,n)
    	x = lista[p:]
    	return x
	else:
        return lista