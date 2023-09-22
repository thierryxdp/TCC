def inverte(frase):
    if ',' and '-' and '.' in frase:
        a = str.replace(frase,',',' ')
        b = str.replace(a,'-',' ')
        c = str.replace(b,'.',' ')
        t = list.reverse(c)
        return t
    if '-' and '!' in frase:
        d = str.replace(frase,'-',' ')
        e = str.replace(d,'!',' ')
        return e
    if '!' in frase:
    	f = str.replace(frase,'!',' ')
    	return f
    if '.' in frase:
        g = str.replace(frase,'.',' ')
        return g
    if '?' in frase:
        h = str.replace(frase,'?',' ')
        return h