def fatorial(n):
    """Calcula o fatorial desse número"""
    """int -> int"""
    
    i=0
    while i < len(list(range(n))):
        fatorial = list(range(n))[i] * list(range(n))[i][i-1]
        
        i = i +1
    return fatorial