def fatorial(n):
    '''Recebe um número e calcula o seu fatorial;
    int -> int'''
    
    f=1
    while n > 0:
        f = f * n
        n = n-1
    return f