def fatorial(n):
    '''retorna o fatorial do numero n; int -> int'''
    i=0
    fatorial=(n-1)
    while i<n:
        fatorial = fatorial*(n-i)
        i=i+1
    return fatorial