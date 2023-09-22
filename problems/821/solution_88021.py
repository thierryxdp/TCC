def fatorial(x):
    '''Retorna o fatorial de um número.
    int -> int'''
    a=x-1
    while a!=1:
        if a==0:
            continue
        x=x*a
        a=a-1
    return x