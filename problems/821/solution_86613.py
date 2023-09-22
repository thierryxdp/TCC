from functools import reduce 
def fatorial (numero:int) -> int:
	"""Função que irá receber um número e retornar o fatorial deste número.
    
    	Parameters: 
        numero: número inteiro que o fatorial será calculado
        
        Returns:
        fatorial do número dado
    """
    
    fatorial = [numero]
    posicao = 1
	sucessor = posicao - 1
    while sucessor > 0:
        fatorial = fatorial + (sucessor)
		posicao = posicao + 1
    return reduce(fatorial)