def inverte(frase):
    """..."""
    x = frase
    y = list.reverse(list(str.lower(x)))
    z = str.join(y)
    return z