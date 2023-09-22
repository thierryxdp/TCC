def fatorial(n:int) -> int:
    """Essa função, dada um número, calcula e retorna seu fatorial"""
    i = 1
    fat = 1
    while i < n:
        fat += 1
        fat *= i
    return fat