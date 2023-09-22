def filtraMultiplos(lista, num):
    
    cont = 0
    multiplos = []
	
    while cont < len(lista):
        if lista[cont] % num == 0:
        	multiplos.append(lista[cont])
            
        cont += 1
   
    return multiplos