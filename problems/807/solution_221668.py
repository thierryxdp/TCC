def conta_frases(frase):
    if '?' and '!' in frase:
        b = str.replace(frase,'?','.')
        return b
    if '!' in frase:
    	a = str.replace(frase,'!','.')
    	return a