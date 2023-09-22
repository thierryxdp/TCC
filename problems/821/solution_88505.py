def fatorial(numero:int) -> int:
    """Essa função, dada um número, calcula e retorna seu fatorial"""
    i = fatorial = 1
    while i < numero:
        i += 1
        fatorial *= i
    return fatorial