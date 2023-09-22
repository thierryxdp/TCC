def uppCons(frase):
	i=0
    ora=frase
    while i<(len(frase)):
        if 'bcdfghjklmnpqrstvwxyz' in frase[i]:
        	str.upper(frase[i])
        	ora=ora+frase[i]
    	i=i+1
    return str.upper(ora)