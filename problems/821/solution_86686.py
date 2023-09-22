def fatorial(n):
    """Retorna o fatorial do número dado."""
    
    fat = 1
    i = 1
    
    while i <= n:
        fat = fat*i
        i = i + 1
        
        return fat