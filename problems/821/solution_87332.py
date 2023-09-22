def fatorial(numero):
    """Calcula o fatorial de um número
       int --> int"""
    i = numero
    j = numero - 1
    fatorial = [numero]
    
    while i != 1 and j != 0:
        numero = numero[i] * numero[j]
		i = i - 1
		j = j - 1
        
	return numero