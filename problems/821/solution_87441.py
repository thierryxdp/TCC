def fatorial(numero):
    soma_do_produto = 0
    produto = 0
    while 0 < numero:
        produto *= numero*(numero-1)
        numero -= 1
    return produto