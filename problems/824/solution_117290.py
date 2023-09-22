def uppCons(frase):
	i=0
    ora=''
    while i<(len(frase)):
        if 'bcdfghjklmnpqrstvwxyz' in frase[i]:
        	ora+str.upper(frase[i])
        if 'aeiouAEIOU' in frase[i]:
            ora+str.lower(frase[i])
    	i=i+1
    return ora