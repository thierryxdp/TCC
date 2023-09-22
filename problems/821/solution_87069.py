def fatorial(numero):
    '''funçao que calcula o fatorial de um numero'''
    while numero > 1:
        fatorial = numero * numero-1
        numero = numero-1
    return fatorial