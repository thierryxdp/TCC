def conta_frases(x):
	interrog=x.count('?')
    exc=x.count('!')
    ponto=x.count('.')
    retcs=x.count('...')
 	
    x1=interrog+exc+ponto+retcs
    x2=interrog+exc+ponto
    if retcs>0 and ponto<6:
        return x1-3
    elif retcs>0 and ponto>=6:
        return x1-6