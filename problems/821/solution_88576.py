def fatorial(numero):
    """..."""
    i = 0
    
    def fatorial(n):
    '''Cacula o fatorial de n.
    int --> int'''
    i = n
    j = 0
    resultado = 0
    while i > 0:
        resultado = resultado * (j+1)
        if i == n:
            resultado = 1
        i -= 1
        j += 1
    return resultado