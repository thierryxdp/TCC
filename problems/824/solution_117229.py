def uppCons(frase):
	i=0
    ora=''
    while i<(len(frase)):
        if 'bcdfghjklmnpqrstvwxyz' in frase[i]:
            str.upper(frase[i])
        ora=ora+str.upper(frase[i])
    	i=i+1
    return ora