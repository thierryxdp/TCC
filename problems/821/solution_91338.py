def fatorial(numero):
    '''Função que recebe um numero do tipo inteiro e retorna o cálculo do
    fatorial deste numero
    int=>int'''
    i=numero-1
    while i > 0:
        numero *= i
        i -= 1
    return numero