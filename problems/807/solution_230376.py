def conta_frases(frase):
    ls=str.count(frase,'.')+str.count(frase,'?')+str.count(frase,'!')
    if('...' not in frase):
        return ls
    if('...'in frase) and ('.'in frase):
    	return str.count(frase,'.')-2
    if('...'in frase) and ('.' not in frase):
        return str.count(frase,'...')
    
	return str.count(frase,'...')