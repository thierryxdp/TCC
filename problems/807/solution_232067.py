def conta_frases(x):
	ponto=str.count(x,'.')
    exc=str.count(x,'!')
	interrog=str.count(x,'?')
    retcs=str.count(x,'...')
	x=ponto+exc+interrog
	return x