def uppCons(frase):
    """..."""
    x = 0
    y = ''
    while x < len(frase):
        if frase[x] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':            
            y = y + str.upper(frase[x])
        elif frase[x] in 'aeiouAEIOU ':
            None
        x = x + 1
    return y