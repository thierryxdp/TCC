def fatorial(n):
    """Calcula o fatorial desse número"""
    """int -> int"""
    
    i = 0
    while i < len(list(range(1,n))):
        fatorial = list(range(1,n))[::-1][i] * list(range(1,n))[::-1][i-1]
        
        i = i + 1
    return fatorial