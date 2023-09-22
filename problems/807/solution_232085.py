def conta_frases(x):
    ponto=x.count('.')
    interrog=x.count('?')
    exc=x.count('!')
    retcs=x.count('...')
    
        
    x=ponto+interrog+exc+retcs
    
    if ponto>=4:
		x=x-3
    
    
    return x