def filtraMultiplos (lista,n): 
    lista1 = []
    i=0
    while i<len(lista) :
        if n % lista[i] == 0 :
        	lista1 = lista1 + lista[i]
        	i = i+1
	return lista1