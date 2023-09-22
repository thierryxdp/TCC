def uppCons(frase):
    """..."""
    frasef = ""
    i = 0
    while (i < len(frase)):
        if frase[i] not in "AEIOUaeiou":
            frasef = frasef[i]+(str.upper(frase[i]))
        i += 1
	return frasef