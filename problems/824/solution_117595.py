def uppCons(frase):
	i=0
    ora=''
    while i<(len(frase)):
        if 'bcdfghjklmnpqrstvwxyz' in frase[i]:
        	str.upper(frase[i])
        	ora=ora+frase[i]
    	i=i+1
    return ora