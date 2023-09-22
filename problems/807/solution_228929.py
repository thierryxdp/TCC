def conta_frases(texto):
    ''' Docs
    str -> int '''

    a = texto
    
	b = a.count('!')
    c = a.count('?')
    d = a.count('.')
    e = a.count('...') 
	
    if '...' in a:
        return (b+c+d)
    
    else:
        return b+c+d+e