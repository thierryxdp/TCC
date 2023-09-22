def maiores(lista,n):
    if min(lista)>n:
    	return list.insert(lista,0,n)
    if max(lista)<n:
        return list.append(lista,n)