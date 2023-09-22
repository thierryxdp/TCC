def uppCons(frase):
    consoantes = 'bcdfghjklmnpqrstvwxyzç'
	i = 0
	while i < len(consoantes):
        frase = frase.replace(consoantes[i],consoantes[i].upper())
    	i = i + 1
	return frase