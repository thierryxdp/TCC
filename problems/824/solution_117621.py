def uppCons(frase):
	i=0
    ora=''
    while i<(len(frase)):
        if 'bcdfghjklmnpqrstvwxyz' in frase[i]:
         str.join(str.upper(frase[i]),ora)
    	else:
         str.join(frase[i],ora)
        i=i+1
    return ora