def fatorial(num):
    """ funcao que, dado um numero num de entrada, retorna o fatorial desse numero
    int--->int"""
    fatorial=1
    while num>1:
        fatorial=fatorial*num
        num=num-1
    return fatorial