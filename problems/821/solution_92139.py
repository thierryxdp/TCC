def fatorial(n):
    """ calcula o fatorial do número 'n'."""
    x = 1
    for f in range(1,n+1):
        x*=f
    return x