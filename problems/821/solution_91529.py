def fatorial(n):
    """Retorna o fatorial de um número inteiro n.
    int -> int"""
    if n == 1:
        return 1
    return n * fatorial(n - 1)