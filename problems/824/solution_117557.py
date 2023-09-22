def uppCons(frase):
	i=0
    while i<(len(frase)):
        if 'bcdfghjklmnpqrstvwxyz' in frase[i]:
        	frase[i]=str.upper(frase[i])
    	i=i+1
    return frase