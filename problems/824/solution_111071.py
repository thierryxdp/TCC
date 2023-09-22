def uppCons(frase):
    """..."""
    fraseupp = str.upper(frase)
    i = 0
    frasef =str()
    while (i<len(fraseupp)):
        if (str.lower(fraseupp[i]) in "aeiou"):
            frasef = (str.lower(fraseupp[i]),)
    	i += 1  
    return str(frasef)