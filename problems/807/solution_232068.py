def conta_frases(x):
	ponto=x.count('.')
    exc=x.count('!')
	interrog=x.count('?')
    retcs=x.count('...')
	x=ponto+exc+interrog+retcs
	return x