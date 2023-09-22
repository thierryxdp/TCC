def fatorial(n):
    """Retorna o fatorial de um número inteiro n.
    int -> int"""
    r = n
    while n > 2:
        r *= n - 1
        n -= 1
    return r