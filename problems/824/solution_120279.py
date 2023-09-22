def uppCons(frase):
    novaFrase = ""
    for l in frase:
        if l in 'bcdfghjklmnpqrstvxwyz':
            novaFrase += str.upper(l)
        else:
            novaFrase += l
            
	return novaFrase