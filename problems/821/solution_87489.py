def fatorial(n):
    '''Dado um numero n, retorna a fatorial deste numero.
    int -> int'''
    i=1
    j=n
    while i<j:
        l=n*(n-i)
        i=i+1
    return l