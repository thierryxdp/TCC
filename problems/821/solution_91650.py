def fatorial(n):
    ''' calcula o fatorial, dada um número n;
    int -> int '''
    i = 1 
    x = 1
    while i<=n:
        x = x*i
        i = i+1
    return x