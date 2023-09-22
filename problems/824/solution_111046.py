def uppCons(frase):
    """..."""
    tupla = tuple(frase)
    i = 0
    frasef = str()
    while (i<len(frase)):
        if (tupla[i] in "bcdfghjklmnpqrstvwxyz"):
            str.upper(frasef[i])
    	i += 1
    
    return frasef