def fatorial(n):
    """retorna o fatorial do numero inserido
    int->int"""    
    i = 1
    n_fat = 1
    
    while i <= n:
        n_fat = n_fat * i
        i = i + 1
    return i