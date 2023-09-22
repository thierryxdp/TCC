def conta_frases(frase):
    if '?' and '!' and '...' in frase:
        i = str.find(frase,'.')
        return frase[0:i]
    if '?' and '!' in frase:
        a = str.replace(frase,'?','.')
        b = str.replace(a,'!','.')
        return b
    if '!' in frase:
    	c = str.replace(frase,'!','.')
    	return c
    if '?' in frase:
        d = str.replace(frase,'?','.')
        return d
    if '.' in frase:
        return frase