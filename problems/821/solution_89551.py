def fatorial(numero):
    '''Funcao que, dado um numero, calcula o fatorial dele; int -> int'''
    x=numero
    while x>=1:
        valor=numero*x
        x=x-1
        return valor