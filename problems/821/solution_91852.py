def fatorial(n):
    """dado um numero,calcula seu fatorial"""
    m=1
    f=1
    while m<n+1:
        f*=m
        m+=1
    return f