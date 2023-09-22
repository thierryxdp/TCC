def fatorial(numero):
    """Calcula o fatorial de um número
       int --> int"""
    i = numero
    j = numero - 1
    fatorial = [numero]
    
    while i != 0 and j != 0:
        fatorial = i * j
		i = i - 1
		j = j - 1
        
	return j