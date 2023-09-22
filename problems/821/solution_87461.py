def fatorial(n):
    """
    	Funcao que recebe um numero.
        Retorna o fatorial desse numero.
        int -> int
    """
    fatorial = 1
    for n_range in list(range(1,n)):
        fatorial = n_range * fatorial
    
    return n_range