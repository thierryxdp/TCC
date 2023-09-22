def posLetra(frase, l, x):
    """..."""
    y = 0
    z = 0
    while y <= x:
        if frase[z] == l:
            y = y + 1
        z = z + 1
    return z