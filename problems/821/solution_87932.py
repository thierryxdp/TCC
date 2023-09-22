def fatorial(n):
    """calcula o fatorial do número n
    int->int"""
    prox=n
    while prox>0:
        n=n*(prox)
        prox=prox-1
    return n