def fatorial(n):
    """Retorna o fatorial do número dado."""
    
    i = 1
    fat = 1
    
    while i <= n:
        fat = fat * i
        i = i + fat
        
        return i