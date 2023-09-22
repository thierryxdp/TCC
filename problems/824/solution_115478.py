def uppCons(frase):
    '''funcao que retorna frase com consoantes em maiusculo.'''
    '''str=>str'''
    s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyçz':
            s += caractere.upper()
        else:
            s += caractere

	return s