def fatorial(numero):
    f = 0
    while numero > 1:
        f = numero*(numero-1)
        numero = numero - 2
    return f