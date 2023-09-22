def fatorial(numero):
    fatorial = 0
    while numero > 1:
        fatorial = fatorial*(numero*(numero-1))
        numero = numero - 2
    return fatorial