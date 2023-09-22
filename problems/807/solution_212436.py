def conta_frases(texto):
    '''Retorna o número de frases de um determinado texto;
    str -> int'''
s=str.count
reticencias=s(texto,'...')
pfinal=s(texto,'.')
pinterrogacao=s(texto,'?')
pexclamacao=s(texto,'!')
	return reticencias+pfinal+pinterrogacao+pexclamacao