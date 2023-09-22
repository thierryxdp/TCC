def uppCons(frase):
    novaFrase = ""
    for l in frase:
        if l in 'aeiou':
            novaFrase += l
        else:
            novaFrase += str.upper(l)
	return novaFrase