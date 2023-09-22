def inverte(frase):
    """..."""
    x = frase
    y = str.lower(x)
    a = list(y)
    a.reverse()
    c = ''.join(a)
    return c