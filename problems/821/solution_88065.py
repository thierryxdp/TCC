def fatorial(n):
    """Calcula o fatorial desse número"""
    """int -> int"""
    
    i=0
    while i < len(list(range(1,n))):
        fatorial = list(range(1,n))[i-1] * list(range(1,n))[i]
        
        i = i +1
    return fatorial