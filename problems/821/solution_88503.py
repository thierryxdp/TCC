def fatorial(n:int) -> int:
    """Essa função, dada um número, calcula e retorna seu fatorial"""
    i = fat = 1
    while i < n:
        i += 1
        fat *= i
    return fat