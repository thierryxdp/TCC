def fatorial(numero):
    '''função que recebe um número e calcula o fatorial deste número.
    int -> complex'''
    fator = numero
    while numero > 1:
        fator = fator * (numero - 1)
        numero -= 1
    return fator