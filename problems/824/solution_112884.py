def uppCons(frase):
    """..."""
    x = 0
    y = list(frase)
    while x < len(y):
        if frase[x] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            str.upper(frase[x])
        else:
            None
    x = x + 1
    return frase