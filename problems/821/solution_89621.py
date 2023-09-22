def fatorial(n):
    """dado um número n, calcula seu fatorial.
    int->int"""
    r=n
    while n>2:
        r=r*(n-1)
    n=n-2
    return r