def uppCons(frase):
    '''
    	A função recebe uma frase e retorna a mesma frase com as suas consoantes 
        todas maiúsculas (e os demais caracteres extamente como estavam na frase 
        original).
        frase -> str
        str -> str
    '''
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            a = frase[i]
            frase[i] = a.upper()
		i += 1
	return frase