def fatorial(n):
    """Calcula e retorna o fatorial de um numero dado.
    int -> int"""
    r = 1
    i = 0
    t = n
    while i in range(t):   
        r = r * n
        n = n - 1
        i = i + 1
    return r