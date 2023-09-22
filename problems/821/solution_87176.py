def fatorial(numero):
    """ Função que recebe um número e retorna o fatorial desse mesmo número.
    int -> int
    """
    c = 1
    fatorial = 1

    while c <= numero:
        fatorial *= c
        c += 1