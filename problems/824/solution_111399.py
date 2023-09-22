def uppCons(frase):
    """.."""
    fraseupp = str.upper(frase)
    frasef = ""
    i = 1
    while(i<len(fraseupp)):
        if fraseupp[i] in "aeiou":
            frasef = frasef+(str.lower(fraseupp[i]))
        elif fraseupp[i] in "bcdfghjklmnpqrstvwxyz":
            frasef = frasef + (fraseupp[i])
        i += 1
	return frasef