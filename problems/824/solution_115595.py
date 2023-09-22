def uppCons(frase):
    '''
    	Recebe uma frase e retorna a mesma frase com as consoantes em maiúsculo
        str -> str
	'''
    i=0
    list(frase)
    '''
    while (i < len(frase)):
        if (frase[i] in 'bcdfghjklmnopqrstvwxyz'):
		frase[i].upper()'''
    a = frase[1].upper()
    frase[1] = a
    return frase[1]