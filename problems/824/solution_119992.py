def uppCons(frase):
	i = 0
	con = ''
	while i<len(frase):
        if frase[i] in 'bcdfghijklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            con_ = con + frase[i]
        i+=1
    ponto=frase.replace(con_,'BCDFGHJKLMNPQRSTVWXYZ')
    return ponto