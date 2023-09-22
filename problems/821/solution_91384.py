def fatorial(numero):
    '''função que dado um número calcula o
    fatorial dele
    int -> int'''
    if numero < 2:
        return 1
    else:
        return numero * fatorial(numero-1)