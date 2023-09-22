def conta_frases(frase):
    if '?' and '!' and '...' in frase:
        i = str.find(frase,'.')
        j = str.find(frase,'!')
        k = i + 1
        1 = frase[0:i]
        2 = frase[k:j]
        return 2
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