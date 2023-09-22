def uppCons(frase):
    i = 0
    oracao = ''
    while i < len(frase):
        msc = frase[i]
		if msc in 'bcçdfghjklmnpqrstvwxyz':
        	msc = str.upper(msc)
        i = i + 1
        oracao = oracao + msc
    return oracao