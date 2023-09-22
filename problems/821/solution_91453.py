def fatorial(numero):
    '''Entrega o valor fatorial do numero requerido
    int-->int'''
    n=0
    f=1
    while numero-n > 0:
        f=f*(numero-n)
        n=n+1
    return f