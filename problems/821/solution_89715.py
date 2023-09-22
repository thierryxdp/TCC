def fatorial(n):
    """ dado um número n, retorna seu fatorial.
    int->int"""
    mult=1
    i=2
    while i<=n:
        mult=mult*i
        i=i+1
    return mult