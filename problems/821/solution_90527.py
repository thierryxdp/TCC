from operator import mul

def fatorial(numero):
    '''funçao que recebe um numero e retorna seu fatoria.
    int -> int'''
    lista=[]
    contador=numero
    while contador>0:
        lista.append(contador)
        contador-=1
    produto = reduce(mul, lista, 1)
    return produto