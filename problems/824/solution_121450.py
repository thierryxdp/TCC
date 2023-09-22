def uppCons(frase):
    consoantes = 'bcdfghjklmnpqrstvxzwy'
    i = 0
    while i < len(frase):
        if frase[i] in consoantes:
            frase[i].upper()
	return frase