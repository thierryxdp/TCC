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
            frase = frase.replace(frase[i],frase[i].upper())
		i += 1
	return frase