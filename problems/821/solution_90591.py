def fatorial(numero):
    """ Funçao que retorna o fatorial de um numero"""
    fatorial = numero
    while numero > 1:
        fatorial = fatorial * (numero-1)
        numero = numero - 1
    return fatorial