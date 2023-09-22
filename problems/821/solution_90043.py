def fatorial(numero):
    '''Retorna o fatorial do número dado
int -> int'''
    fatorial=1
    while numero>0:
        fatorial=fatorial*numero
        numero=numero-1
    return fatorial