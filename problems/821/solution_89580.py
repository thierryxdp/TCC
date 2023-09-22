def fatorial(n):
    """Dado um numero é calculado o fatorial desse numero.
    	int-->int"""
    i=0
    a=n
    while i<n:
        f=n*(a-1)
        i=i+1
        a=a-1
    return f