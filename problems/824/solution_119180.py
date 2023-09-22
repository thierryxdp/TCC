def uppCons(x):
    x = str.upper(x)
	Frase = [""]
    for frase in x:
        if frase == "A":
            frase = frase + "a"
        elif frase == "E":
            frase = frase + "e"
        elif frase == "I":
            frase = frase + "i"
        elif frase == "O":
            frase = frase + "o"
        elif frase == "U":
            frase = frase + "u"
        
		else:
            frase = frase
	return frase