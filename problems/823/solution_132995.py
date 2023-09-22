def faltante(lista):
    i = 1    
    while i < len(lista):
        if lista[i] != (i + 1):
        	break
		if lista[i] == (i + 1):
    		i += 1
    return i