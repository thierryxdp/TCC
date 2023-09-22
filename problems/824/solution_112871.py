def uppCons(frase):
    """..."""
    x = 0
    y = list(frase)
    z = []
    while x < len(y):
        if str(y[x]) in ['BCDFGHJKLMNPQRSTVWXYZ']:
            z = z + y[x]
        else:
            None
        x = x + 1
    return z