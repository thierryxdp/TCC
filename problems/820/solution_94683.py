def posLetra(string, letra, n):
    i = 0
    k = 0
    lista = list(string)
    
    if list.count(lista) < n:
        return -1
    else:
    	while k < n:
        	if lista[i] == letra:
            	k += 1
        	i += 1
    
    return i-1