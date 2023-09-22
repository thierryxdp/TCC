def fatorial(num):
    """ funcao que, dado um numero num de entrada, retorna o fatorial desse numero
    int--->int"""
    fatorial=num
    while num>1:
        fatorial=fatorial*(num-1)
    return fatorial