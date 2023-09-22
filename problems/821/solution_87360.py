def fatorial(numero):
    """Calcula o fatorial de um número
       int --> int"""
    i = numero - 1
    ocorrencia = 0
    fatorial = numero
    
    while i != 0:
        fatorial *= i
        ocorrencia += 1
		i = i - 1
        
	return fatorial