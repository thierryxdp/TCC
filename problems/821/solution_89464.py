def fatorial(x):
    '''
    calcula o fatorial de x
    int->int
    '''
    i=x
    fatorial=1
    while i>0:
        fatorial=fatorial*i
        i=i-1
    return fatorial