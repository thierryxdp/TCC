def fatorial (numero:int) -> int:
	"""Função que irá receber um número e retornar o fatorial deste número.
    
    	Parameters: 
        numero: número inteiro que o fatorial será calculado
        
        Returns:
        fatorial do número dado
    """
    
    fatorial = 1
    i = 1
    while i <= numero:
        fatorial = fatorial * i
		i = i + 1
    return fatorial