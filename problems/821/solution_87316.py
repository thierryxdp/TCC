def fatorial(numero):
    """Calcula o fatorial de um número
       int --> int"""
    i = numero
    j = numero - 1
    
    while i != 1 and j != 1:
        fatorial = fatorial[i] * fatorial[j]
		i = i - 1
		j = j - 1
        
	return fatorial