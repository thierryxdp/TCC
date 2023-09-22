def uppCons(frase):
    """..."""
    frasef = ""
    i = 0
    while (i < len(frase)):
        if frase[i] not in "AEIOUaeiou":
            frasef = frasef+(str.upper(frase[i]))
        elif frase[i] in "AEIOUaeiouãáéíóúõ":
            frasef =  frasef+(frase[i])
        i += 1
	return frasef