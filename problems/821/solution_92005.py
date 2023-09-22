def fatorial(numero):
    """Dado um numero, retorna seu fatorial"""
    if numero <=1:
        return 1
    n=numero-1
    x=1
    while n>1:
        x=x*numero*n
        n-1
    return x