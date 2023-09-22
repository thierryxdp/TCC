def conta_frases(texto):
    '''Retorna o número de frases de um determinado texto;
    str -> int'''
s=str.count
reticencias=s(texto,'...')
p_final=s(texto,'.')
p_interrogacao=s(texto,'?')
p_exclamaçao=s(texto,'!')
	return reticencias+p_final+p_interrogacao+p_exclamaçao