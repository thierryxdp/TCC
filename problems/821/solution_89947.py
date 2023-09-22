def fatorial (numero):
    '''Dado um número, retorne com o fatorial dele;
    int -> int'''
    i = 0
    n = 1
    num = numero
    while i< numero:
        n = n*num
        num = num - 1
        i = i + 1
        return n