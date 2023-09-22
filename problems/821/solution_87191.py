def fatorial(n):
    """ Calcula o fatorial do número n.
    	int -> int
        
        Parameter:
        n: Número n.
        
        Returns:
        Fatorial do número dado.
    """
    i = 1
    res = n
    while n - i > 1:
        res = res * (n - i)
        i  = i + 1
    return res