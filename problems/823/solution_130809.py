def faltante(lista):
    
    lista.sort()
    lista1 = list(range(lista[0], lista[-1]))
    cont = 0
    
    while cont < len(lista):
    
    	if lista[cont] != lista1[cont]:
        	return lista[cont]        	
        
        else:
            cont += 1