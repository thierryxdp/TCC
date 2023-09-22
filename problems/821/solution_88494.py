def fatorial(n:int) -> int:
    """Essa função, dada um número, calcula e retorna seu fatorial"""
    i = 1
    fatorial = 1
    while i < n:
        fatorial *= i
    i += 1
    return fatorial