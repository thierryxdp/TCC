def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            frase.replace(frase[1],frase[1].upper())
        	i=i+1
    		return frase