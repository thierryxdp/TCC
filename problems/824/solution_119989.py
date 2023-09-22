def uppCons(frase):
	i = 0
	con = ''
	while i<len(frase):
        if frase[i] in 'bcdfghijklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            con = con + frase[i]
        i+=1
    ponto=frase.replace('b','B')
    return frase