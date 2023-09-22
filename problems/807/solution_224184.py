def conta_frases(texto):
    "Retorne o numero de frases de um dado texto; str->int"
    x=str.count(texto,'.')
    y=str.count(texto,'...')
    z=str.count(texto,'!')
    w=str.count(texto,'?')
    
	if x=3 and y=1:
        return y+z+w
    if y>0:
    	return (x+y+z+w)-(x-y)
	else:
        return (x+y+z+w)