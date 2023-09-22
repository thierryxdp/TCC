def fatorial(numero):
    """ Função que dado um número calcule o fatorial deste número. Insira um número inteiro e não negativo
    	int -> int
    """
    
    if numero == 0:
        return 1
    
    resposta = numero
    
    while numero > 2:
        numero = numero - 1 
        resposta = resposta * numero
        
    return resposta