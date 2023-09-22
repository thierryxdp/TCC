def qtd_divisores(n):
    """ Funcao que conta quantos divisores um numero tem;
    	int -> int
    """
    divisores = 0
    numeros_entre_1_n = range(1, n)
    
    for numero in numeros_entre_1_n:
        if n % numero == 0:
            divisores += 1
            
    return divisores