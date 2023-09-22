def conta_frases(frase):
    if '.' in frase:   
    	a = list.count(frase, '.')
    	b = str.replace(frase,'.',',',a)
    	return b