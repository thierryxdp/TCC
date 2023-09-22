def conta_frases(frase):
    ls=str.count(frase,'.')+str.count(frase,'?')+str.count(frase,'!')
    if('...' not in frase):
        return ls
    if('...'in frase) and ('.'in frase):
    	return str.count(frase,'.')-2
    
	return str.count(frase,'..')