def fatorial(numero):
    multiplicacao = numero
    while numero > 1:
        multiplicacao *= numero - 1
        numero -= 1

    return multiplicacao