def fatorial(n):
    """retorna a fatorial do numero n"""
    """int -> int"""
    i = 1
    f = n
    while i <= n:
        f = n*i
    i += 1    
    return f