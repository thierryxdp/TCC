def uppCons(frase):
    i = 0
    cons = ''
    while i < len(frase):
        if not (frase[i] in "AEIOUaeiou"):
            cons += frase[i].upper()
        i += 1
	return cons