def fatorial(n):
    """calcula e rettorna o fatorial de n; int -> int"""
    a=n
    while a>0:
        a=a*n
        n=n-1
    return a