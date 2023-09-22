def fatorial (n):
    """calcula o fatorial de um número dado"""
    f=0
    while n!=0:
        f=n*(n-1)
        n=n-1
    return f