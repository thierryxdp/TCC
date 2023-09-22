def uppCons(frases):
    i=0
    aux = ''
    while i < len(frases):
    	if frase[i] in 'bcdfghjklmnpqrstvxwyzç':
        	aux += frases[i].upper()
    	else:
        	aux += frases[i]
    	i += 1
    return aux