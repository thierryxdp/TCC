def fatorial(n):
    """dado um número n, calcula seu fatorial.
    int->int"""
    r=n
    while r>2:
        n=n*(n-1)
    r=r-2
    return r