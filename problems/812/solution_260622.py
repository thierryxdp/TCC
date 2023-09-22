def retira_pontuacao(frase):
    if ',' and '.' in frase:
        d = str.replace(frase,',',' ')
        e = str.replace(d,'.',' ')
        return e
    if '!' in frase:
    	a = str.replace(frase,'!',' ')
    	return a
    if '.' in frase:
        b = str.replace(frase,'.',' ')
        return b
    if '?' in frase:
        c = str.replace(frase,'?',' ')
        return c