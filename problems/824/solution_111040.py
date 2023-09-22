def uppCons(frase):
    """..."""
    tupla = tuple(frase)
    i = 0
    while (1<len(frase)):
        if (tupla[i] in "bcdfghjklmnpqrstvwxyz"):
            str.upper(frase[i])
    	i += 1
    
    return frase