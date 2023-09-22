def fatorial(n):
    """Calcula e retorna o fatorial de um numero dado.
    int -> int"""
    r = 1
    i = -1
    t = n
    while i in range(t):
        i = i + 1
        r = r * n
        n = n - 1
    return r