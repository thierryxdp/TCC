def maiores(lista,n):
    if min(lista)>n:
    	list.insert(lista,0,n)
        return lista
    if max(lista)<n:
        list.append(lista,n)
 		return lista