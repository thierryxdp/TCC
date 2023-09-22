def uppCons(frase):
    """..."""
    frasef = ""
    i = 0
    while (i < len(frase)):
        if frase[i] in "bcdhjklmnpqrstvwxyz":
            frasef = frasef+(str.upper(frase[i]))
        i += 1
	return frasef