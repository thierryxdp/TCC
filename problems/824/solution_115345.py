def uppCons(frase):
    '''str->str
    '''
    i=0
    string='-'
    while i<len(frase):
    	if frase[i]!= 'AIUEOaiueo':
        	frase[i].upper()
  		i+=1
  	return frase