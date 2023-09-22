def fatorial(numero):
    '''Função que dado um número de entrada, calcula o fatorial desse mesmo
    número.'''
    fatorial = 1
    contador = 2
    while contador <= numero:
        fatorial = fatorial * contador
        contador = contador + 1
    return fatorial