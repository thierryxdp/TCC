def uppCons(frase):
	i = 0
	con = ''
	while i<len(frase):
        if frase[i] in 'bcdfghijklmnpqrstvwxyz':
            con = con + frase[i]
        i+=1
    return con.upper(i)