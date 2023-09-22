def fatorial(numero):
    """dado um numero, calcula o fatorial desse mesmo numero
    int --> int"""
    i = 0
    fatorial = 1
    numero2 = numero
    while i < numero:
        fatorial = fatorial * numero2
        numero2 = numero2 - 1
        i = i + 1
    return fatorial