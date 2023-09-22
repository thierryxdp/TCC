def fatorial(n):
    '''Dado um numero n, retorna a fatorial deste numero.
    int -> int'''
    i=0
    j=n
    while i<j:
        n=n*(n-1)
        i=i+1
    return i