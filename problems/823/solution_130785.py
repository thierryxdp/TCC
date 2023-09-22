def faltante(lista):
    
    lista.sort()
    cont = 0
    
    while cont < len(lista):
    
    	if lista[0] != 1:
        	return 1
    
    	elif (lista[cont+1] - lista[cont]) != 1:
            return lista[cont]
        	cont += 1
        
        else:
            pass