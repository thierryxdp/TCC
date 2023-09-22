def fatorial(num):
    """."""
    c = contador = 1
    while contador < num:
        contador += 1
        c *= contador
    return c