def uppCons(frase):
    i=0
    while i<len(frase):
		if not frase[i] in 'aeiouAEIOU':
            str.upper(frase[i])
        i=i+1
    return frase