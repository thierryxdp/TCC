def fatorial (numero:int) -> 
	"""Função que irá receber um número e retornar o fatorial deste número.
    
    	Parameters: 
        numero: número inteiro que o fatorial será calculado
        
        Returns:
        fatorial do número dado
    """
    
    fatorial = [numero]
    posicao = 1
    while [numero - [posicao]] > 0:
        fatorial = fatorial + [numero - posicao]

    return numpy.prod(fatorial)