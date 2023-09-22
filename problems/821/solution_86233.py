def fatorial(n):
    """Esta é a função que dado um número retorna seu fatorial; int -> int"""
    n = int(n)
    fatorial = 1
    
    while n > 0:        
            fatorial = fatorial * n
            n = n - 1
        
    return fatorial