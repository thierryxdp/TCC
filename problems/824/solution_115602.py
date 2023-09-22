def uppCons(frase):
    '''
    	Recebe uma frase e retorna a mesma frase com as consoantes em maiúsculo
        str -> str
	'''
    i=0
    result = ''
    while (i < len(frase)):
        if (frase[i] in 'bcdfghjklmnopqrstvwxyz'):
			result = result + frase[i].upper()
        else:
            result = result+frase[i]
    	i+=1
    
    return len(frase)