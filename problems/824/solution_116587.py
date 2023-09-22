def uppCons(frase:str)->str:
    '''retorna a frase com as consoantes em maiúsculas'''
    i=0
    retorno = ''
    while i <len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            retorno += frase[i].upper()
		else:
            retorno += frase[i]
		i += 1        
	return retorno