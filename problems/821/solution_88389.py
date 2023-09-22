def fatorial(n):
    """Calcula e retorna o fatorial de um numero dado.
    int -> int"""
    r = 1
    t = n
    i = 0
    while i <= t:
        r = r * n
        n = n-1
    	i += 1
    return r