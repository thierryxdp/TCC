def fatorial (n):
    """ Dado um número n, calcula o fatorial desse número.
    entrada int -> saida int."""
    
    fatorial = 1
    
    while n > 0:
        fatorial = fatorial*n
        n = n-1
    return fatorial