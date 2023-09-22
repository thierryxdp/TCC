def fatorial(numero):
    """Calcula o fatorial de um número
       int --> int"""
    i = numero
    j = numero - 1
    fatorial = [numero]
    
    while i != fatorial[i] and j != fatorial[j]:
        fatorial = fatorial[i] * fatorial[j]
		i = i - 1
		j = j - 1
        
	return fatorial