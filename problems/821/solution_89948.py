def fatorial (numero):
    '''Dado um número, retorne com o fatorial dele;
    int -> int'''
    i = 0
    f = 1
    numf = numero
    while i < numero:
        f = f*numf
        numf = numf - 1
        i = i + 1
    return f