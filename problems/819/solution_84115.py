def filtraMultiplos (lista, n):
    """ dado uma llista e um numero n, retorna uma nova lista contendo apenas os elementos da lista anterior que são multiplos do numero n.
    entrada lista de int, int ->  saida lista int."""
    
    multiplos = []
    
    i = 0
	while i<len(lista):
    	if lista[i]%n == 0:
            multiplos = multiplos + [lista[i]]
    	i = i+1 
    return multiplos