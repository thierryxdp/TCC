def fatorial(num):
    """ Recebe um numero e retorna seu fatorial;
    int->int """
    fatorial=1
    n=1
    while n<=num:
        fatorial=fatorial*n
        n=n+1
    return fatorial