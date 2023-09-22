def fatorial(numero):
    produto = 1
    while 0 < numero:
        produto = produto*numero*(numero-1)
        numero -= 1
    return produto