def conta_frases(frases):
    
	x = str.count(frases, '.')
	x += str.count(frases, '?')
	x += str.count(frases, '!')
	a = str.count(frases, '...')

    
	return x + a