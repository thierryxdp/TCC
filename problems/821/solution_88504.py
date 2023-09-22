def fatorial(n:int) -> int:
    """Essa função, dada um número, calcula e retorna seu fatorial"""
    i = fatorial = 1
    while i < n:
        i += 1
        fatorial *= i
    return fatorial