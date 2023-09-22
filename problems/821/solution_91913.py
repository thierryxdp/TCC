def fatorial (n):
    """calcula o fatorial de um número dado"""
    f=1
    while n!=0:
        f=n*f
        n=n-1
    return f