def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou! ,.?ãâÃÂ':
            str.upper(frase[i])
        else:
            frase[i]=frase[i]
        i=i+1
        	return frase