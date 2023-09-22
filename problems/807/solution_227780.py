def conta_frases(frases):
    
	x = str.count(frase, '.')
	y = str.count(frase, '?')
	z = str.count(frase, '!')
	a = str.count(frase, '...')

    
	return a + x + y + z