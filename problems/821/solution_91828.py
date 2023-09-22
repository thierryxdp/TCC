def fatorial(numero):
    """Essa função recebe um numero e calcula seu fatorial
    int -> int"""
    fatorial = 0
    while numero > 1:
        fatorial= fatorial + (numero * (numero-1))
        numero -= 1
    return fatorial