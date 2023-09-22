def uppCons(frase):
    """..."""
    frasef = ""
    i = 0
    while (i < len(frase)):
        if frase[i] not in "AEIOUaeiou":
            frasef = frasef+(str.upper())
        i += 1
	return frasef