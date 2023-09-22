def uppCons(frase):
    '''str->str
    '''
    i=0
    while i<len(frase):
    	if frase[i]!= 'AIUEOaiueo':
            frase[i].upper()
  		i+=1
    return frase