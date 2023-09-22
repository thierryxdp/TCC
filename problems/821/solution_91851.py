def fatorial(n):
    """dado um numero,calcula seu fatorial"""
    m=2
    f=1
    while m!=n:
        f*=m
        m+=1
    return f