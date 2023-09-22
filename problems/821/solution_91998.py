def fatorial(numero):
    """Dado um numéro, retorna seu fatorial"""
    n=0
    resultado=()
    while n<=numero:
        resultado=n*(n+1)
        n=n+1
    return resultado