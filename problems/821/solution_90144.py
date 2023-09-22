def fatorial(n):
    """
    
    """
    valor=n*(n-1)
    n-=2
    while n>0:
        valor=valor*n
        n-=1
    return valor