def filtraMultiplos(numeros,n):
    '''Retorna todos os multiplos de n da lista numeros.
    lista, float --> lista'''
    i = 0
	multiplos = []
    while(i < len(numeros)):
        if(numeros[i] % n == 0):
            multiplos[len(multiplos):len(multiplos)] = [numeros[i]]
            
        i += 1
        
	return multiplos