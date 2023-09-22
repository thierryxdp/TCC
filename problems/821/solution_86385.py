def fatorial(número):
    '''Calcula o fatorial de certo número dado
    int -> int'''
    i = 0
    fatorial = [ ]
    while i < número:
        if número % i == 0:
            fatorial = fatorial + [i]
        else:
            i = i + 1
            return fatorial