def fatorial(numero):
    '''
    Dado um número, retorna seu fatorial.
    int-> int
    '''
    i = 0
    f = 1
    numero1 = numero
    while i < numero:
        fat = fat * numero1
        numero1 = numero1 - 1
        i = i + 1
    return f