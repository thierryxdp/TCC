def fatorial(n):
    """Calcula o fatorial desse número"""
    """int -> int"""
    
    fatorial = 0
    i = 1
    while i < len(list(range(1,n))):
        fatorial += list(range(1,n))[::-1][i-1] * list(range(1,n))[::-1][i]
        
        i = i + 1
    return fatorial