def conta_frases(frase):
	'''funaçao que conta o numero de frases presntes em um texto;
    str->int'''
    
    
    if str.count(frase,'...')>1:
    	n = -(3*str.count(frase,'...'))
    else:
        n=0
    
    
    
    n = n + str.count(frase,'...')
	n = n +str.count(frase,'!')
	n = n + str.count(frase,'?')
	n = n + str.count(frase,'.')
    
    
    return n