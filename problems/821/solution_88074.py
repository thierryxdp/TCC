def fatorial(n):
    """Calcula o fatorial desse número"""
    """int -> int"""
    
    i = len(list(range(1,n)))
    while i < len(list(range(1,n))):
        fatorial = list(range(1,n))[i] * list(range(1,n))[i-1]
        
        i = i - 1
    return fatorial