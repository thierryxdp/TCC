def fatorial(n):
    '''Recebe um numero e retorna seu fatorial
    int ->int'''
    i=0
    fatorial=1
    while i<n:
        fatorial= fatorial*(n-i)
        i=i+1
    return fatorial