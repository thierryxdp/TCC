def conta_frases(x):
	interrog=x.count('?')
    exc=x.count('!')
    ponto=x.count(' . ')
    retcs=x.count('...')
 	
    x1=retcs+ponto+exc+interrog
    x2=ponto+exc+interrog
   
	if retcs>0:
        return x1
    else:
        return x2