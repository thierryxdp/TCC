def fatorial(n):
    """função que dado um número 'n', retorne o fatorial de 'n';int-->float"""
    fatorial=1
    x=1
    while x<=n:
        fatorial=(fatorial*x)
        x=x+1
    return fatorial