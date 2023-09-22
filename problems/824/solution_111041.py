def uppCons(frase):
    """..."""
    tupla = tuple(frase)
    i = 0
    while (i<len(frase)):
        if (tupla[i] in "bcdfghjklmnpqrstvwxyz"):
            str.upper(frase[i])
    	i += 1
    
    return frase