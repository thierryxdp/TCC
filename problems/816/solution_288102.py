def maiores(lista, n):
    if n not lista:
        lista.append(n)
    	lista.sort()
    	x = lista.index(n)
    	lista2 = lista[x+1:]
    	y = lista2.count(n)
    	return lista2[y:]