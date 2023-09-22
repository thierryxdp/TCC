def fatorial(n):
    """
    	Funcao que recebe um numero.
        Retorna o fatorial desse numero.
        int -> int
    """
    if n < 2:
        return 1
    
    return fatorial(n - 1) * fatorial(n)