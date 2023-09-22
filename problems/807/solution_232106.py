def conta_frases(x):
	interrog=x.count('?')
    exc=x.count('!')
    ponto=x.count('. ')
    retcs=x.count('...')
 	
    x=interrog+exc+ponto+retcs
    return x