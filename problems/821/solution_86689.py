def fatorial(n):
    """Retorna o fatorial do número dado."""
    
    fat = 1
    i = 2
    
    while i <= n:
        fat = fat*i
        i = i + 1
        
        return i