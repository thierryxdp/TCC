def filtra_pares(tupla):
	pares = ()
    if tupla[0]%2 == 0:
        pares += (tupla[0],)
    else:
    	if tupla[1]%2 == 0:
        	pares += (tupla[1],)
        else:
    		if tupla[2]%2 == 0:
       			pares += (tupla[2],)
            else:
    			if tupla[3]%2 == 0:
                pares += (tupla[3],)
    			return pares