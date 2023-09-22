def uppCons(frase):
    i=0
    while i<len(frase):
        i=i+1
        if frase[i] not in 'AEIOUaeiou! ,.?ãâÃÂ':
            str.upper(frase[i])
        else:
            frase[i]=frase[i]
        	return frase