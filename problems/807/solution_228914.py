def conta_frases(texto):
    ''' Docs
    str -> int '''

    a = texto
    
	b = a.count('!')
    c = a.count('?')
    d = a.count('...')
	
    return b + c + d