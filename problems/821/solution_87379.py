def fatorial(n):
    '''retorna o fatorial do numero n; int -> int'''
    i=1
    fatorial=n
    while i<n:
        fatorial = fatorial*(n-i)
        i=i+1
    return fatorial