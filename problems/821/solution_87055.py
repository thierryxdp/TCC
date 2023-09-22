def fatorial(numero):
    """Dado um número, retorne seu fatorial.
    int -> int"""

    fatorial = 1

    while numero >= 2:
        fatorial = fatorial * numero
        numero -= 1
    return fatorial