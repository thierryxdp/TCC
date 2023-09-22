def fatorial(n):
    '''retorna o fatorial do numero n; int -> int'''
    i=0
    fatorial=1
    while i<n:
        fatorial = n*(n-i)
        i=i+1
    return fatorial