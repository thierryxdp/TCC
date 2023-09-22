def uppCons(frase):
	i = 0
	con = ''
	while i<len(frase):
        if frase[i] in 'bcdfghijklmnpqrstvwxyz':
            con=con + frase.replace(frase[i],' ')
        i+=1
    ponto=con.replace(' ','B')
    return ponto