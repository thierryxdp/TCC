def fatorial(numero):
    """Calcula o fatorial de um número
       int --> int"""
    i = numero
    j = numero - 1
    fatorial =[]
    
    while i < len(fatorial) and j < len(fatorial):
        	fatorial = fatorial[i] * fatorial[j]
        		i -= 1
        		j -= 1
        
	return fatorial