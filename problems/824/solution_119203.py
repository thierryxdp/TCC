def uppCons(x):
    x = str.upper(x[1:])
	r = ""
    for frase in x:
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
        
		else:
            r = r + frase
	return r