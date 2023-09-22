def filtra_pares(t):
    if type(t) == tuple and len(t) == 4:
    	lista = []
    	for i in t:
        	if i%2 == 0:
            	lista.append(i)
            	return(tuple(lista))