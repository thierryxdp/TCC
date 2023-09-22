def fatorial(n):
    """
    
    """
    valor=0
    while n>1:
        valor+=n*(n-1)
        n-=2
    return valor