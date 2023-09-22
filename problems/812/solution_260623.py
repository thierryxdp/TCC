def retira_pontuacao(frase):
    if ',' and '-' and '.' in frase:
        a = str.replace(frase,',',' ')
        b = str.replace(a,'-',' ')
        c = str.replace(b,'.',' ')
        return c 
    if '!' in frase:
    	g = str.replace(frase,'!',' ')
    	return g
    if '.' in frase:
        h = str.replace(frase,'.',' ')
        return h
    if '?' in frase:
        t = str.replace(frase,'?',' ')
        return t