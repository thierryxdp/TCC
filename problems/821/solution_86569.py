def fatorial(n):
    '''Dado um número n, calcule seu fatorial; int -> int'''
    fatorial=1
    while n>0:
        fatorial=fatorial*n
        n=n-1
    return fatorial
    if n==0:
        return 1