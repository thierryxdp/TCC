def fatorial(numero):
    '''Funcao que, dado um numero, calcula o fatorial dele; int -> int'''
    x=numero-1
    produto=numero
    while x>=1:
        produto*=x
        x-=1
    return produto