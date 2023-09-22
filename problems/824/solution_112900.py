def uppCons(frase):
    """..."""
    x = 0
    y = ''
    while x < len(frase):
        if frase[x] in 'b' or 'c' or 'd' or 'f' or 'g' or 'h'or'j'or'k'or'l'or'm'or'n'or'p'or'q'or'r'or's'or't'or'v'or'w'or'x'or'y'or'z':            
            y = y + str.upper(frase[x])
        else:
            None
        x = x + 1
        return y