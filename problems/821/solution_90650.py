def fatorial(numero):
    '''Recene um numero e calcula o fatorial deste numero.
    int -> int'''
    i = numero
    f = 1
    while i > 0:
        f *= i
        i -= 1
       	return f