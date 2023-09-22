def uppCons(x):
    x = str.upper(x)
	r = ""
    for frase in x:
        if frase == "A":
            r = frase + "a"
        elif r == "E":
            r = frase + "e"
        elif frase == "I":
            r = frase + "i"
        elif frase == "O":
            r = frase + "o"
        elif frase == "U":
            r = frase + "u"
        
		else:
            r = r + r
	return r