def fatorial(n):
    """Dado um numero é calculado o fatorial desse numero.
    	int-->int"""
    i=1
    while n>0:
        i=i*n
        n=n-1
    return i