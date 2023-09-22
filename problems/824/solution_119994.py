def uppCons(frase):
	i = 0
	con = ''
	while i<len(frase):
        if frase[i] in 'b':
            con=con + frase.replace(frase[i],'B')
        if frase[i] in 'c':
            con = con + frase.replace(frase[i],'C')
        i+=1
    
    return ponto