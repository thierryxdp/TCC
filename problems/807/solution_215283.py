def conta_frases(texto):
    """Função que retorna a quantidade de frases presentes no texto dado"""
	a = str.replace(texto,'?','#')
	b = str.replace(a,'!','#')
	c = str.replace(b,'.','#')
	d = str.replace(c,'...','#')
	e = str.split(d,'#')
	return len(e)