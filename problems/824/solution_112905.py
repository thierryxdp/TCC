def uppCons(frase):
    """..."""
    x = 0
    y = ''
    while x < len(frase):
        if frase[x] in 'bcdfghjklmnpqrstvwxyz':            
            y = y + str.upper(frase[x])
        elif frase[x] in 'a' or 'b' or 'c' or 'd' or 'e':
            None
        x = x + 1
    return y