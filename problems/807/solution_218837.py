def conta_frases(txt):
	a = txt.count('...')
    if a > 0:
    	x = a*3
        b = txt.count('.') - x
    c = txt.count('!')
    d = txt.count('?')
    return a+b+c+d