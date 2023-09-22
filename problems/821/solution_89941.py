def fatorial (numero):
    '''Dado um número, retorne com o fatorial do mesmo;
    int -> int'''
    i = 0
    n = 1
    num = numero
    while i<numero:
        n = n*num
        i = i +1
        return n