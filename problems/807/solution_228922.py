def conta_frases(texto):
    ''' Docs
    str -> int '''

    a = texto
    
	b = a.count('!')
    c = a.count('?')
    d = a.count('.')
    e = a.count('...') //3
	
    return (b + c + d + e)