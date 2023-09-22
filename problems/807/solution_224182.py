def conta_frases(texto):
    "Retorne o numero de frases de um dado texto; str->int"
    x=str.count(texto,'.')
    y=str.count(texto,'...')
    z=str.count(texto,'!')
    w=str.count(texto,'?')
    if y>0:
    	return (x+y+z+w)-(x-y)
	else:
        return (x+y+z+w)