def fatorial(numero):
    '''função que dado um número retorna seu fatorial'''
    if numero < 2:
        return 1
    else:
        return numero * fatorial(numero-1)