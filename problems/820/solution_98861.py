def posLetra(frase, l, x):
    """..."""
    y = list(frase)
    if x in y:
        z = list.index(y, l, x, -1)    
    return z
    else:
        return '-1'