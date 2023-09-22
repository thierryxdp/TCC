def fatorial(n):
    """Calcula e retorna o fatorial do número n.
    int -->  int"""
    
    fatorial = 1
    i = 2
    
    while i <= n:
        
        fatorial = fatorial*i
        i = i + 1
        
    return fatorial