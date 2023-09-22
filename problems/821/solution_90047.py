def fatorial(n):
    '''Calcula o fatorial do número n, int -> int'''
    i=0
    fatorial=1
    while i<n:
        fatorial= fatorial*(n-i)
        i+=1
    return fatorial