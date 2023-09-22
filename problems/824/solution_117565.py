def uppCons(frase):
	i=0
    ora=frase
    while i<(len(frase)):
        if 'bcdfghjklmnpqrstvwxyz' in frase[i]:
           ora[i]=str.upper(frase[i])
        if 'AEIOUaeiou' in frase[i]:
           ora[i]=frase[i]
    i=i+1
    return ora