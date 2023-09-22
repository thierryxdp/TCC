def uppCons(frase):
    """..."""
    x = 0
    while x < len(frase):
        if frase[x] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            str.upper(frase[x])
        else:
            None
        x = x + 1
        return frase