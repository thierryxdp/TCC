def fatorial(n:int) -> int:
    """Essa função, dada um número, calcula e retorna seu fatorial"""
    i = 1
    f = 1
    while i < n:
        f += 1
        f *= i
    return f