def fatorial (numero):
    """ retorne o fatorial do numero.
    int -> int"""
    n = numero
    contador = 1
    while n > 0:
        contador *= n
        n -= 1
    return contador