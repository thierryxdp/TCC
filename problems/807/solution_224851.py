def conta_frases(frase):
	'''funaçao que conta o numero de frases presntes em um texto;
    str->int'''
    
    
    n=0
    n = n + str.count(frase,'...')
	n = n +str.count(frase,'!')
	n = n + str.count(frase,'?')
	n = n + str.count(frase,'.')
    
    if str.count(frase,'...')>1:
    	n = n-(3*str.count(frase,'...'))
    
  	return n