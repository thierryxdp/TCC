def fatorial(n):
    """Recebe um número e retorna seu fatorial.
    int -> int"""
    i = n
    valor = 1
    while i > 0:
        valor *= i
        i -= 1
    return valor