def uppCons(frase):
	i=0
    ora=frase
    while i<(len(frase)):
        if 'bcdfghjklmnpqrstvwxyz' in frase[i]:
           ora[i]=ora+str.upper(frase[i])
        if 'AEIOUaeiou' in frase[i]:
           ora[i]=ora+frase[i]
    	i=i+1
    return ora