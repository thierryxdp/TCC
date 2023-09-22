def tirapont(frase):
    if ',' and '-' and '.' in frase:
        a = str.replace(frase,',',' ')
        b = str.replace(a,'-',' ')
        c = str.replace(b,'.',' ')
        return c 
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
def inverte(frase):
	t=list.reverse(tirapont(frase))
    return t