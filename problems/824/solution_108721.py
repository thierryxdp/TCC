def uppCons(frase):
    '''retorna uma frase com todas consoantes em maiusculo'''
    '''str->str'''
    cont = 0
    palavra = ''
    while cont < len(frase):
        if frase[cont] in 'bcdfgçhjklmnpqrstvwxz':
            k = str.upper(frase[cont])
            palavra = palavra + k
            cont += 1
		else:
            palavra = palavra + frase[cont]
            cont += 1
	return palavra