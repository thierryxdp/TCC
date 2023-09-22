def soma_h(n):
    """ Calcula o valor H com N termos.
    	int -> float
        
        Parameter:
        n: Número n.
        
        Returns:
        Valor da soma H.
    """
    i = 1
    soma = 0
    while i <= n:
        soma = soma + (1/i)
        i = i + 1
    return round(soma, 2)