def fatorial(n):
    """ dado um número 'n', retorna o fatorial deste número.
    int->int """
    fatorial=1
    if n=0:
        return 1 
    while n>=1:
        fatorial = fatorial*n
        n = n-1
    return fatorial