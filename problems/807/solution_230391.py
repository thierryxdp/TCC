def conta_frases(frase):
    ('.' is not '...')
    
    ls=str.count(frase,'.')+str.count(frase,'?')+str.count(frase,'!')+str.count(frase,'...')
	if('...' in frase):
		return ls-3
    if('...' in frase) and ('.' in frase):
        return ls-6
    return ls