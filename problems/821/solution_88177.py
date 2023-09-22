def fatorial(n):
    """Calcula o fatorial desse número"""
    """int -> int"""
    
    fatorial = n
    i = n
    lista = list(range(1,n))
    while i>= 1:
        fatorial = fatorial*(fatorial-1)
        i = i - 1
    return fatorial