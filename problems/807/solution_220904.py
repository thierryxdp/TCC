def conta_frases(texto):
    '''Dado um texto, retorna a quantidade de frases. str-->int'''
	return str.count(texto,'.') + str.count(texto,'!') + str.count(texto,'?') -2* str.count(texto,'...')