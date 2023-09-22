def fatorial(numero):
    for indice in list(range(10)):
        if indice == 0:
            fatorial = 1
        fatorial = fatorial * indice
    return fatorial