def fatorial(numero):
    '''Função que dado um número calcula o fatorial deste número.
    int -> int'''
    i = numero - 1
    while i > 0:
        numero = numero * i
        x = numero
        i = i - 1
    if numero == 1:
        return 1
    else:
        return x