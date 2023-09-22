def maiores(lista,n):
    type(lista) == list and type(n) == int
    lista.append(n)
    for i in lista:
	    if i<n:
		    lista.remove(i)
    lista_ordenada=sorted(lista)
    return lista_ordenada