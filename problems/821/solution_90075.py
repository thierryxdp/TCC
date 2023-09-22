def fatorial(numero):
    '''Função, que dado um número, calcula o fatorial deste número.'''
    '''int->int'''
    fatorial = 1
    proximo = 0
    while numero>1:
        fatorial = fatorial  * numero
        numero = numero - 1
    proximo = proximo + 1 
    return fatorial