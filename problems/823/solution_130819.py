def faltante(lista):
    
    lista.sort()
    lista1 = list(range(lista[0], len(lista) + 1))
    cont = 0
    
   ''' while cont < len(lista):
    
    	if lista[cont] != 1:
            return 1
        
        elif lista[cont] != lista1[cont]:
        	resultado = lista1[cont]        
        
        else:
            return lista[cont] + 1
            
        
        cont += 1'''
   
	return lista1