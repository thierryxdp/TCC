def fatorial(numero):
    '''Recene um numero e calcula o fatorial deste numero.
    int -> int'''
    i = 0
    while i < numero:
        i -= numero
        fatorial = numero * i
        return fatorial