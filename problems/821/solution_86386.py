def fatorial(numero):
    '''Calcula o fatorial de certo número dado
    int -> int'''
    i = 0
    fatorial = [ ]
    while i < numero:
        if numero % i == 0:
            fatorial = fatorial + [i]
        else:
            i = i + 1
            return fatorial