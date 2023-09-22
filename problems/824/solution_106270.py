def uppCons(frase):
    i = 0 
    while i < len(frase):
        if not frase[i] in "AEIOUaeiou":
            frase[i] = frase[i].upper()
        i += 1
	return frase