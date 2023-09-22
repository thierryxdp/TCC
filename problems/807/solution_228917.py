def conta_frases(texto):
    ''' Docs
    str -> int '''

    a = texto
    
	b = a.count('!')
    c = a.count('?')
    d = a.count('.') - 3
    e = a.count('...') 
	
    return b + c + d + e