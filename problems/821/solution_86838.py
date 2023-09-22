from math import prod
def fatorial(x):
    '''Escreva um numero qualquer. A funcao retorna o fatorial
    desse numero.
    int -> int'''
    i=0
    fatorial=()
    while x-i!=1:
        fatorial=fatorial+(x-i)
        i=i+1
    return prod(fatorial)