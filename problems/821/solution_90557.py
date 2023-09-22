def fatorial(numero):
    ''' função que ao receber um número retorna o seu fatorial
        int ---> int '''
    a = 1
    fatorial = numero
    while a != numero:
        fatorial = fatorial * a
        a += 1
    return fatorial