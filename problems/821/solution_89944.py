def fatorial (numero):
    '''Dado um número, retorne com o fatorial do mesmo;
    int -> int'''
    i = 1
    n = 1
    while i<=numero:
        n = n*numero
        i = i + 1
        return n