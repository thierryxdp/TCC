def fatorial(n):
    """
    	Recebe um número <n> e retorna seu fatorial.
        int --> int
    """
    i = 0
    fatorial = 1
    while i < n:
        fatorial *= n - i
        i += 1
    
    return fatorial