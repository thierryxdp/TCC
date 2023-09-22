def fatorial(n):
    """dado um número n, calcula seu fatorial.
    int->int"""
    r=1
    while n>1:
        r=r*n
    n=n-1
    return r