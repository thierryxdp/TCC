def fatorial(n):
    """Calcula e retorna o fatorial de um numero dado.
    int -> int"""
    r = 1
    i = 0
    while i in range(n):
        i = i + 1
        r = r * n
        n = n - 1
    return r