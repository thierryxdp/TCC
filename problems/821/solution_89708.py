def fatorial(n):
    """dado um número n, calcula seu fatorial.
    int->int"""
    r=n-1
    while r>2:
        n=n*(n-r)
    r=r-2
    return n