def conta_frases(frase):
    if '?' and '!' in frase:
        b = str.replace(frase,'?','.')
        c = str.replace(b,'!','.')
        return c
    if '!' in frase:
    	a = str.replace(frase,'!','.')
    	return a
    if '.' in frase:
        return frase