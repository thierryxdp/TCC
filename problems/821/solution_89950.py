def fatorial(numero):
    '''dado um numero, retorna o seu fatorial
    int->int'''

    i = 0
    fatorial = 1
    numero2 = numero
    while i < numero:
        fatorial = fatorial * numero2
        numero2 = numero2 - 1
        i = i + 1
    return fatorial