def uppCons(x):
    x = str.upper(x)
	r = ""
    for frase in x:
        if frase == "A":
            r = r + "a"
        elif r == "E":
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
        
		else:
            r = r + frase
	return r