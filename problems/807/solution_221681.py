def conta_frases(frase):
    if '?' and '!' and '...' in frase:
        e = str.replace(frase,'?','.')
        f = str.replace(e,'!','.')
        g = str.replace(f,'...','.')
        i = str.find(frase,'.')
        g[0:i] = 1
        st = g[0:1]
        return st
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