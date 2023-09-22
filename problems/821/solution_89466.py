def fatorial(numero):
    '''Calcula o fatorial do número dado
    int->int'''
    i=0
    fatorial=0
    while i<=numero:
        fatorial=fatorial*i
        i=i+1
    return fatorial