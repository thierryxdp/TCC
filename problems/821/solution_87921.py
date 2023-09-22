def fatorial(n):
    """Funcao que calcula o fatorial de um numero; int -> int"""
    
    fatorial = 1
    
    while n > 0:
        fatorial = fatorial * n
        n = n - 1
    return fatorial