def uppCons(frase):
    """..."""
    x = 0
    y = list(frase)
    while x < len(y):
        if str(y[x]) in ['bcdfghklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ']:
            str.upper(str(y[x]))
        else:
            None
        x = x + 1    
    ''.join(y)
    return y