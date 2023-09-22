def uppCons(frase):
    """..."""
    tupla = tuple(frase)
    i = 0
    while (i<len(tupla)):
        if (tupla[i] in "bcdfghjklmnpqrstvwxyz"):
            str.upper(tupla[i])
    	i += 1
    
    return tupla