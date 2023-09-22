def fatorial(numero):
    '''Esta função calcula o fatorial de um número dado.
int->int'''
    fatorial=1
    while numero>0:
        fatorial=numero*fatorial
        numero=numero-1
    return fatorial