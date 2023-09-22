def fatorial(n):
    """calcula e rettorna o fatorial de n; int -> int"""
    a=n
    c=1
    while a>0:
        c=c*a
        a=n-1
    return c