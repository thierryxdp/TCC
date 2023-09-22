def fatorial(n):
    """enquanto n>0, multiplicamos o fatorial=1 pelo valor de n-1 ate n=0
    int -> int"""
    t=n
    fato=1
    while t>0:
        fato= fato*t
        t=t-1
    return fato