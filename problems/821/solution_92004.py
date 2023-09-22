def fatorial(numero):
    """Dado um numero, retorna seu fatorial"""
    if numero<=1:
        return numero*fatorial(numero-1)