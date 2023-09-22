def fatorial(numero):
    '''Funcao que recebe um numero e retorna o fatorial deste numero'''
    contador = 1
    fatorial = 1
    while contador <= numero:
        fatorial *= contador
        contador += 1
    return fatorial