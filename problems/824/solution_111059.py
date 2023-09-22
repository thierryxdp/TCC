def uppCons(frase):
    """..."""
    tupla = tuple(frase)
    i = 0
    frasef =tuple()
    while (i<len(tupla)):
        if (str.lower(tupla[i]) in "bcdfghjklmnpqrstvwxyz"):
            frasef += (str.upper(tupla[i]),)
    	i += 1
    
    return frasef