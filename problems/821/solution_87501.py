def fatorial(n):
    '''Dado um numero n, retorna a fatorial deste numero.
    int -> int'''
    i=0
    j=n
    while i<j:
        i=i+1
        n=(n-j)*(n-i)
    return n