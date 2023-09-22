def fatorial(numero):
    """Calcula o fatorial de um número
       int --> int"""
    i = numero
    j = numero - 1
    ocorrencia = 0
    fatorial = 0
    
    while i != 0 and j != 0:
        fatorial = i * j
        ocorrencia += 1
		i = i - 1
		j = j - 1
        
	return fatorial * ocorrencia