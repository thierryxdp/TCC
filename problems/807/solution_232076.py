def conta_frases(x):
	retcs=x.count('...')
    exc=x.count('!')
	interrog=x.count('?')
    ponto=x.count('. ')
    pomto=x.count('.')
	x=retcs+exc+interrog+ponto+pomto
	return x