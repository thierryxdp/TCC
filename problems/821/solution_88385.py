def fatorial(n):
    """Calcula e retorna o fatorial de um numero dado.
    int -> int"""
    r = 1
    for i in range(n):
        r = r * n
        n = n-1
    return r