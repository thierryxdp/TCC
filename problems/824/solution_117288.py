def uppCons(frase):
	i=0
    ora=''
    while i<(len(frase)):
        if 'bcdfghjklmnpqrstvwxyz' in frase[i]:
        	ora+str.upper(frase[i])
        else:
            ora+str.lower(frase[i])
    	i=i+1
        ora=ora+str(frase[i])
    return ora