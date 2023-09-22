def fatorial(numero):
    """A função retorna o fatorial de um número.
    int-->int."""
    i = 1
    fatorial = numero
    while i < numero:
        fatorial = fatorial * i
        i += 1
    return fatorial