def fatorial(n_fat):
    """retorna o fatorial do numero inserido
    int -> int"""
    
    i = range(n_fat)
    
    
    while i <= n_fat:
        n_fat = n_fat * i
        i = i + 1
        
        return n_fat