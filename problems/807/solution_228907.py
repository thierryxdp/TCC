def conta_frases(texto):
    ''' Docs
    str -> int '''

    a = texto
	b = str.count(a, '.', '!')
    c = str.count(a, , '?', '...')
	
    return b + c