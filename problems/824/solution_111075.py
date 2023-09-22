def uppCons(frase):
    """..."""
    fraseupp = str.upper(frase)
    i = 0
    x = str()
    while (i<len(fraseupp)):
        if (fraseupp[i] in "aeiou"):
            x += (str.lower(fraseupp[i]))
    	i += 1  
    return x