def conta_frases(x):
	retcs=x.count('...')
    exc=x.count('!')
	interrog=x.count('?')
    ponto='.'
    pomto=x.count(ponto)
	x=retcs+exc+interrog+pomto
	return x