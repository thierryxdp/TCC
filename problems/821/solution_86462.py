def fatorial(numero):
    """recebe um numero e retorne o fatorial desse numero; int->int"""
    fatorial = 1
    while (numero > 1):
        fatorial = fatorial * numero
        numero = numero - 1
    return fatorial