def fatorial(numero):
    total = 1
    while numero > 0:
        total = total*numero
        numero = numero - 1
    return total