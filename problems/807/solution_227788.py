def conta_frases(frases):
    ''' dada uma frase returna o número de frases separadas por . ! ? e ...
    	str --> int'''
    
	x = str.count(frases, '.')
	x += str.count(frases, '?')
	x += str.count(frases, '!')
	a = str.count(frases, '...')

    
	return (x + a) - 3*a