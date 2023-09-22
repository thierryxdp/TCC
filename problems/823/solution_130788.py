def faltante(lista):
    
    lista.sort()
    cont = 0
    tam = (len(lista) - 1)
    
    while cont < tam:
    
    	if lista[0] != 1:
        	return 1
    
    	elif (lista[cont+1] - lista[cont]) != 1:
            return lista[cont]
        	
        
        else:
            pass  
        
   	return lista[]