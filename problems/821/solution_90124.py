def fatorial(numero):
    '''Função que dado um número calcula o fatorial deste.'''
    #int -> int
    i = 1
    fatorial = 1
    while i <= numero:
        fatorial = fatorial * i 
        i = i + 1
    return fatorial