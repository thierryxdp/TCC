def fatorial(x):
    '''recebe um numero(x) e retorna seu fatorial. int->int'''
    y = x
    fatorial = x
    while y>1:
        y = y-1
        fatorial = fatorial*y
    return fatorial