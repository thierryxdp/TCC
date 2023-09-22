def uppCons(x):
    x = str.upper(x)
    return x
    z = x[0:1]
    y = x.upper(1:)
	r = ""
    for frase in y:
        if frase == "A":
            r = r + "a"
        elif frase == "E":
            r = r + "e"
        elif frase == "I":
            r = r + "i"
        elif frase == "O":
            r = r + "o"
        elif frase == "U":
            r = r + "u"
        elif frase == "Ã":
            r = r + "ã"
        elif frase == "Ó":
            r = r + "ó"
        elif frase == "Ó":
            r = r + "ó"
        elif frase == "Ú":
            r = r + "ú"
        elif frase == "Í":
            r = r + "í"
        elif frase == "É":
            r = r + "é"
		else:
            r = r + frase
	return z + r