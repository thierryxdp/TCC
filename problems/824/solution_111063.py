def uppCons(frase):
    """..."""
    i = 0
    frasef =str()
    while (i<len(frase)):
        if (str.lower(frase[i]) in "bcdfghjklmnpqrstvwxyz"):
            frasef += (str.upper(frase[i]),)
    	i += 1
	    
    return frasef