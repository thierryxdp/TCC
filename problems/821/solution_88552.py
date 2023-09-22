def fatorial(n):
    """Essa função, dado um número, calcula e retorna seu fatorial"""
    fatorial = n
    i = 1
    while i < n:
        fatorial = fatorial*i
        i = i + 1
    return fatorial