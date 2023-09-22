def uppCons(frase):
    """..."""
    i = 0
    frasef =tuple()
    while (i<len(frase)):
        if (str.lower(frase[i]) in "bcdfghjklmnpqrstvwxyz"):
            frasef += (str.upper(frase[i]),)
    	i += 1
		    
    return str(frasef)