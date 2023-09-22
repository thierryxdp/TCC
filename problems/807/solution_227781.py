def conta_frases(frases):
    
	x = str.count(frases, '.')
	y = str.count(frases, '?')
	z = str.count(frases, '!')
	a = str.count(frases, '...')

    
	return a + x + y + z