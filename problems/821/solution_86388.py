def fatorial(numero):
    '''Calcula o fatorial de certo número dado
    int -> int'''
    i = 2
    fatorial = ['1']
    while i < numero:
        if numero % i == 0:
            fatorial = fatorial + [i]
        else:
            i = i + 1
            return fatorial