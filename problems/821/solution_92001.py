def fatorial(numero):
    """Dado um numero, retorna seu fatorial"""
    if numero<=1:
        return 1
    n=1
    while n<=numero:
        prod=(numero)*numero-(1*n)
        n+1
    return prod