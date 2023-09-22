def uppCons(frase):
    """..."""
    i = 0
    while (1<len(frase)):
        if (frase[i] in "bcdfghjklmnpqrstvwxyz"):
            str.upper(frase,frase[i])
    	i += 1
    
    return frase