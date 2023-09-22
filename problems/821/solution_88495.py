def fatorial(n:int) -> int:
    """Essa função, dada um número, calcula e retorna seu fatorial"""
    c = cont = 1
    while cont < n:
        cont += 1
        c *= cont
    return c