def fatorial(numero):
    for indice in list(range(numero)):
        if indice == 0:
            fatorial = 1
        else:
            fatorial = fatorial * indice
    return fatorial