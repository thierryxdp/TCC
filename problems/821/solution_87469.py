def fatorial(n):
    '''Dado um numero n, retorna a fatorial deste numero.
    int -> int'''
    fator=n
    i=0
    while i<n:
        n=n*(n-i)
        i=i+1
        return n