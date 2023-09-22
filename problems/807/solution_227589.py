def conta_frases(texto):
    '.'!='...'
	n1=str.count(texto,'.')
	n2=str.count(texto,'!')
	n3=str.count(texto,'?')
	n4=str.count(texto,'...')  
	return n1+n2+n3+n4