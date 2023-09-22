def filtraMultiplos(lista1, n):
    
    """Funçao que filtra os multiplos de um numero(n).Entrada: lista1 e n. retorna outra lista contendo os multiplos"""
    
    multiplos = []
    proximo = 0
    
    while proximo < len (lista1):
        
        if lista1 [proximo] % (n) == 0:
            
            multiplos = multiplos + [lista1[proximo],]
		proximo = proximo + 1
        
	return multiplos