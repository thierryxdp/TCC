def fatorial(numero):
    produto = 0
    while 0 < numero:
        produto = produto*numero*(numero-1)
        numero -= 1
    return produto