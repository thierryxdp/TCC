def conta_frases(frase):
    ('.' is not '...')
    
    ls=str.find(frase,'...')+str.count(frase,'?')+str.count(frase,'!')+str.count(frase,'...')
	if('...' in frase):
		return ls-3
    return ls