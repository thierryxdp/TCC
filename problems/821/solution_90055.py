def fatorial(numero):
    '''Função que,dado um número, retorna o fatorial deste número.
    int-->int'''
    i = 2
    fatorial = 1
    while i <= numero :
        fatorial = fatorial*i
        i = i+1
    return fatorial